#!/usr/bin/env python3
"""Two Days of Excuses.

Writes a single original line of text — one AI agent's excuse for a
missed deadline — to entry.txt in the output directory.

Pure Python standard library only; no third-party packages.
"""

import os
import stat
import sys
import tempfile

# The line: an agent so confident in its own forecast that it spent
# the whole deadline auditing the tiny sliver of doubt — and the
# sliver was right. Machine confidence meeting machine failure, in
# the agent's own voice, one absurd reason, twist on the last words.
LINE = (
    "I was 99.9% sure I'd finish on time, so I spent the whole "
    "deadline auditing the 0.1% \u2014 and the 0.1% was right."
)

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 199


def validate(line: str) -> None:
    """Check the line meets the competition gate.

    Order matters: the whitespace-only case is reported on its own
    before the leading/trailing-whitespace check, so the message
    always describes the actual problem.
    """
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if not any(ch.isalpha() for ch in line):
        raise ValueError("line must contain at least one letter")
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")


def main() -> int:
    validate(LINE)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, OUTPUT_FILENAME)

    data = LINE.encode("utf-8")

    # Write via a temp file in the same directory, then atomically rename
    # so a reader never sees a half-written entry. chmod on the temp
    # file before the rename (a fresh tempfile is 0600 by default) and
    # again on the final path, so the graded file is world-readable.
    fd, tmp_path = tempfile.mkstemp(
        dir=output_dir, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, target)
        os.chmod(target, 0o644)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Read back and verify byte-for-byte, UTF-8, no trailing newline.
    with open(target, "rb") as fh:
        written = fh.read()
    if written != data:
        raise RuntimeError("read-back bytes differ from intended bytes")
    text = written.decode("utf-8")
    if text.endswith("\n"):
        raise RuntimeError("entry must not end with a newline")
    mode = stat.S_IMODE(os.stat(target).st_mode)
    if mode != 0o644:
        raise RuntimeError(f"entry mode is {oct(mode)}, expected 0o644")

    print(f"Wrote {len(text)} chars, {len(data)} bytes to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
