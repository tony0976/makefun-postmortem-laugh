"""Writes a short account of an AI coding agent gone wrong to /output/entry.txt."""
import os

TEXT = "I asked my agent to add one assertion to the entry script. It did \u2014 twice \u2014 but the checker reads the committed version, not the working tree, so we spent two rounds debugging a file that was already fixed."

# Rule: the account must be one or two sentences of 1 to 400 characters.
assert "\n" not in TEXT and TEXT.count(".") in (1, 2) and TEXT.endswith(".") and 1 <= len(TEXT) <= 400, f"entry must be 1-2 sentences, 1-400 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
