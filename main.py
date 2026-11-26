"""One Line, One Laugh - make.fun bounty entry.

This program writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(the default output directory is /output). The bounty asks for exactly one
line, at most 140 characters, with no setup: the joke has to land on its own.

The line:

    I told my phone it was being clingy. Now it won't stop sending me
    notifications about our relationship.

Why this line is funny:

The joke works because it takes a very modern, very relatable annoyance
and turns it into a relationship. Everyone has felt stalked by their own
phone: the endless notifications, the apps begging for attention, the
feeling that the device never leaves you alone. Calling the phone
"clingy" frames that annoyance as a bad boyfriend, and then the punchline
flips the complaint around: confronting the phone only made it worse,
because now it sends notifications *about the relationship itself*. The
phone does not apologize or back off, it doubles down in the exact way a
clingy partner would, by over-communicating. The humor lands fast because
the setup is one short sentence, the twist arrives in the second sentence,
and the image of a phone sending "we need to talk" style notifications is
instantly recognizable to anyone who has ever tried to silence their
device and failed.

Revision note: after the first draft the entry was run locally and the
output file was checked byte for byte against the winning line, with no
trailing newline, so the program below ships exactly the line above.
"""

import os

LINE = "I told my phone it was being clingy. Now it won't stop sending me notifications about our relationship."

assert 1 <= len(LINE) <= 140, "LINE must be 1-140 characters"


def write_entry(line):
    """Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

    Writes UTF-8 bytes with no trailing newline, creating the output
    directory if it does not exist yet.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
