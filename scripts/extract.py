import csv
import json
import re
import sys
from pathlib import Path


def extract(path):
    text = open(path).read()
    date_str = path.name[-13:-3]
    match = re.search(r"Praise\? ([^ ]+) (.+) (to|at) <?jsvine", text)
    verb, core, preposition = match.groups()
    fifth_hed = re.findall(r"\n\s*__(.*?)__", text)[-1]

    return {
        "date": date_str,
        "verb": verb,
        "core": core,
        "preposition": preposition,
        "fifth_hed": fifth_hed.replace("\\", ""),
    }


def generate_output(paths, output_dir):
    extracted = list(map(extract, paths))

    with open(output_dir / "phrases.json", "w") as f:
        json.dump(extracted, f, indent=2)

    with open(output_dir / "phrases.csv", "w") as f:
        fieldnames = list(extracted[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted)


if __name__ == "__main__":
    input_dir = Path("archive/editions")
    output_dir = Path("data")
    paths = sorted(input_dir.glob("*.md"))
    generate_output(paths, output_dir)
