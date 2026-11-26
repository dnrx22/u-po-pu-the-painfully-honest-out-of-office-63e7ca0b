#!/usr/bin/env python3
"""Write one painfully honest out-of-office auto-reply to entry.txt.

Deterministic, stdlib only, no network.
"""
import os
import sys

REPLY = (
    "I'm on leave and my inbox is already out of control. "
    "I'll reply on my return, slowly and honestly, "
    "in the order I can bear to open them. "
    "Thank you for your patience."
)


def main() -> int:
    reply = REPLY
    if not reply or not reply.strip():
        print("error: reply is empty", file=sys.stderr)
        return 1
    if "\n" in reply or "\r" in reply:
        print("error: reply must be a single line", file=sys.stderr)
        return 1
    if len(reply) > 200:
        print(f"error: reply is {len(reply)} characters, over 200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(reply)
    print(reply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
