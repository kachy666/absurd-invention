"""One-sentence absurd invention pitch for make.fun.

The invention: a Wi-Fi router that refuses to connect until you
apologise out loud — a sincerity toll for getting online — and
then, the moment it hears sarcasm in your apology, retaliates by
throttling you down to dial-up speed. The joke is the router
acting as a petty, tone-policing gatekeeper: connection is earned
by contrition, and the wrong tone costs you the modern internet.
This module checks the pitch against the competition rules and,
when it passes, writes it out to /output/entry.txt.
"""

PITCH = "A Wi-Fi router that only connects after you apologise out loud, and drops you to dial-up speed the moment it detects sarcasm."

MAX_CHARS = 220


class PitchError(ValueError):
    """Raised when the pitch breaks one of the competition rules."""


def check_pitch(text):
    """Check the pitch against every rule and return it unchanged.

    Rules enforced here:
      * not empty
      * no leading or trailing whitespace
      * no newline, carriage return, or tab characters
      * no other control characters
      * at most MAX_CHARS characters long
      * exactly one sentence (no sentence-ending . ! ? followed by a space)
      * ends with a period
    """
    if not text:
        raise PitchError("pitch must not be empty")

    if text != text.strip():
        raise PitchError("pitch must not start or end with whitespace")

    if "\n" in text or "\r" in text or "\t" in text:
        raise PitchError("pitch must not contain a newline, carriage return, or tab")

    for character in text:
        if ord(character) < 32:
            raise PitchError("pitch must not contain control characters")

    if len(text) > MAX_CHARS:
        raise PitchError(
            "pitch is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )

    for index, character in enumerate(text):
        if character in ".!?" and index + 1 < len(text) and text[index + 1] == " ":
            raise PitchError(
                "pitch must be exactly one sentence: a sentence-ending . ! ? followed by a space splits it into two"
            )

    if not text.endswith("."):
        raise PitchError("pitch must end with a period")

    return text


def main():
    """Validate the pitch and write it to /output/entry.txt."""
    checked = check_pitch(PITCH)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(checked + "\n")


if __name__ == "__main__":
    main()
