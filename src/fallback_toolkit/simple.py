import functools
from collections import defaultdict





def fallback(id=None):
    def decorator(func):

        _id = id or func.__name__

        fallabck_obj = fallback_registry.get(_id)
        if fallback_obj is None:
            fallback_obj = Fallback(_id)
            fallback_registry[_id] = fallback_obj

        fallback_obj = fallback_registry[_id]
        fallback_obj.add(func)

        @functool.wraps(func)
        def wrapper(*args, **kwargs):
            return fallback_obj(*args, **kwargs)

        return wrapper
    return decorator


class FallbacksFailed(Exception):
    pass


class Fallback:
    def __init__(self):
        self.functions = []


    def add(self, func):
        self.functions.append(func)


    def __call__(self, *args, **kwargs):
        self.exceptions = []
        for _func in self.functions:
            try:
                return _func(*args, **kwargs)
            except Exception as e:
                self.exceptions.append(e)

        raise FallbacksFailed()


fallback_registry = dict()

