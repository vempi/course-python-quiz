#!/usr/bin/env python3
import sys
sys.path.insert(0, 'd:\\OneDrive\\Projects-BOOK\\hydrolab')

try:
    from tasks import PACKAGES
    print("SUCCESS: PACKAGES imported")
    print(f"Total packages: {len(PACKAGES)}")
    for k, v in sorted(PACKAGES.items()):
        print(f"  ID {k}: {v['name']}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
