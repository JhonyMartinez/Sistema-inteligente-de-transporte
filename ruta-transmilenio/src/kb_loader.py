import json
from typing import Any

def load_json(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_stations(path: str):
    return load_json(path)

def load_edges(path: str):
    return load_json(path)

def load_rules(path: str):
    return load_json(path)