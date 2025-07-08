from functools import wraps
from typing import Any, Callable


def cache (func: Callable) -> Any:
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(*args)
        else:
            print("Calculating new result")
            cache_dict = func(*args)
            cache_dict[args] = cache_dict
            return cache_dict
    return wrapper

