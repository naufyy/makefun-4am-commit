"""One-line commit message for the 4am-commit bounty.

Writes the proxy-tournament winning line (C2, 5-0 in the Groq round-robin)
to /output/entry.txt: an agent's 4am commit after a long night fixing the
bugs it wrote itself, each fix unspooling the previous one, back to lunch.
"""
from pathlib import Path

ENTRY = "4am: removed the bug I wrote at 2am, which fixed the bug I wrote at midnight, which was patching the bug from lunch"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
