from typing import Dict, Any, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    if key in dct:
        return dct[key]
    else:
        return default
