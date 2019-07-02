from pathlib import Path
import os
import mimetypes


root = Path(__file__).parent
tz = root / "tz"


def is_binary(filename):
    try:
        with open(filename, "r") as f:
            for l in f:
                text = l
        return False
    except UnicodeDecodeError:
        return True  # Fond non-text data


for x in tz.glob('**/*'):
    if "." in str(x.name):
        continue
    if x.is_file() and is_binary(str(x)):
        print("Renamed", x, "->", str(x) + ".tz")
        os.rename(str(x), str(x) + ".tz")
