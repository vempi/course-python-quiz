"""Simple heuristic AI code detector — score kode berdasarkan pola ChatGPT/Claude."""

import re


def detect_ai_patterns(code: str) -> dict:
    """
    Analisis kode dan return dict dengan:
    - risk_score: 0-100 (0=pasti human, 100=pasti AI)
    - flags: list of detected patterns
    """
    flags = []
    score = 0

    # 1. Excessive comments (ChatGPT sering over-comment)
    comment_lines = len([l for l in code.split('\n') if l.strip().startswith('#')])
    total_lines = len([l for l in code.split('\n') if l.strip()])
    if total_lines > 0 and comment_lines / total_lines > 0.35:
        flags.append("Komentar terlalu banyak (over 35% baris)")
        score += 15

    # 2. Unused imports
    imports = re.findall(r'^import (\w+)|^from (\w+)', code, re.MULTILINE)
    imports = set(str(x).replace("('", "").replace("', '')", "") for x in imports if x)
    used = set(re.findall(r'\b(' + '|'.join(re.escape(i) for i in imports) + r')\b', code))
    if len(imports) > 0 and len(used) / len(imports) < 0.7:
        flags.append("Ada import yang tidak digunakan")
        score += 10

    # 3. Generic/formal variable names that are unusual
    generic_names = re.findall(r'\b(temp_var|temporary|placeholder|result_set|data_frame|output_list)\b', code)
    if generic_names:
        flags.append(f"Nama variabel generik/formal: {', '.join(set(generic_names))}")
        score += 12

    # 4. Perfect code structure (no debugging, no typos, no retries)
    # Human code biasanya ada: typos, variable reassignment, trial-and-error
    # AI code biasanya langsung sempurna
    if code.count('=') > 3 and code.count('==') == 0:  # Many assignments but no conditionals
        if 'try:' not in code and 'except' not in code:
            flags.append("Struktur kode terlalu rapi (tidak ada error handling atau debugging)")
            score += 18

    # 5. Verbose print statements (ChatGPT loves extra prints)
    print_count = len(re.findall(r'print\(', code))
    if print_count > 8 and total_lines < 40:
        flags.append(f"Terlalu banyak print() statements ({print_count})")
        score += 15

    # 6. Markdown-style comments (copy-paste from ChatGPT output)
    if '---' in code or '===' in code or re.search(r'#+ \w+', code):
        flags.append("Gaya komentar seperti markdown (pattern ChatGPT)")
        score += 20

    # 7. Type hints everywhere (not typical for beginner Python)
    if re.findall(r':\s*(str|int|float|list|dict|bool)', code):
        type_hints = len(re.findall(r':\s*(str|int|float|list|dict|bool)', code))
        if type_hints > 5:
            flags.append(f"Banyak type hints ({type_hints}) — tidak umum untuk level pemula")
            score += 12

    # 8. Perfect docstrings
    if '"""' in code or "'''" in code:
        docstrings = len(re.findall(r'""".*?"""|\'\'\'.*?\'\'\'', code, re.DOTALL))
        if docstrings > 2:
            flags.append("Docstrings formal (pattern ChatGPT)")
            score += 15

    # 9. Lambda functions (biasanya human beginner tidak pakai)
    if 'lambda' in code and code.count('\n') < 30:
        flags.append("Penggunaan lambda (tidak umum untuk pemula)")
        score += 10

    # 10. Perfect error handling
    if code.count('try:') > 2 and code.count('except') > 2 and len(flags) == 0:
        flags.append("Error handling terlalu lengkap (tidak umum untuk first attempt)")
        score += 15

    # Clamp to 0-100
    score = min(100, max(0, score))

    # Risk level
    if score >= 70:
        risk_level = "🚨 SANGAT TINGGI"
    elif score >= 50:
        risk_level = "⚠️ TINGGI"
    elif score >= 30:
        risk_level = "⚡ SEDANG"
    else:
        risk_level = "✓ RENDAH"

    return {
        "score": score,
        "risk_level": risk_level,
        "flags": flags,
    }
