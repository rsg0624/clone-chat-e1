import json
from pathlib import Path

DATA = Path(__file__).parent / "personalities.json"

def get_personality(name="funny"):
    with open(DATA) as f:
        personalities = json.load(f)
    return personalities.get(name, personalities["funny"])
