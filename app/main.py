from functools import wraps
from typing import Any, Callable, Dict, Tuple


def cache (func: Callable) -> Any:
    func_cache: Dict[Tuple, Any] = {}
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        if args in cache_dict:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[cache_key] = result
            return result
    return wrapper

