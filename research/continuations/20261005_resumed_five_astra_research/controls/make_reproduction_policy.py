#!/usr/bin/env python3
"""Write a bounded macOS policy for this copied controls directory; run nothing."""
import json
from pathlib import Path


def main():
    controls = Path(__file__).resolve().parent
    credentials = "[private local path removed]"
    policy = (
        "(version 1)\n"
        "(allow default)\n"
        "(deny network*)\n"
        "(deny file-read* (subpath " + json.dumps(credentials, ensure_ascii=False) + "))\n"
        "(deny file-write* (require-not (subpath "
        + json.dumps(str(controls), ensure_ascii=False) + ")))\n"
    )
    target = controls / "reproduction_sandbox.sb"
    target.write_text(policy, encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
