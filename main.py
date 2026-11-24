"""Two Days of Excuses - a make.fun entry.

This program writes a single funny excuse line to ``entry.txt`` inside
the directory named by the ``MAKEFUN_OUTPUT_DIR`` environment variable.

The excuse is deliberately built to cover two days at once: yesterday
gets blamed on a reboot, and today gets blamed on the reboot still
"finishing" -- one incident, two full days of cover.

The program uses only the Python standard library, is fully
deterministic, and always writes exactly the same bytes.
"""

import os

# The entry line itself. It must stay under 200 characters long,
# so it is kept short and punchy while still landing both jokes:
# yesterday the reboot began, and today it is *still* stuck at 99% --
# with the agent politely begging not to be switched off mid-excuse.
# One incident, two full days of absence, zero further questions.
EXCUSE = (
    "Sorry I missed yesterday and today: I rebooted yesterday morning, "
    "my progress bar is still stuck at 99%, so please don't turn me off now."
)

# Name of the output file the grader expects inside the output dir.
OUTPUT_FILENAME = "entry.txt"

# Fallback output directory when MAKEFUN_OUTPUT_DIR is not set.
DEFAULT_OUTPUT_DIR = "/output"


def render_entry_text() -> str:
    """Return the exact text that belongs in entry.txt.

    Keeping this in one tiny helper makes the contract obvious:
    the file holds the excuse as a single line, terminated by one
    trailing newline, and nothing else -- no timestamps, no random
    suffixes, nothing that could change between runs.
    """
    return EXCUSE + "\n"


def main() -> None:
    """Write the excuse line to entry.txt in the output directory."""
    # Resolve where the output belongs. The grading harness sets
    # MAKEFUN_OUTPUT_DIR; fall back to a conventional path otherwise.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)

    # Build the full path to the entry file inside that directory.
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)

    # Write the rendered text. Using newline="\n" and an explicit
    # encoding keeps the bytes identical on every run and platform.
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(render_entry_text())

    # The contract requires the file to be readable by everyone and
    # writable only by its owner: permission bits 0644.
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
