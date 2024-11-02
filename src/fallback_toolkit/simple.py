import functools
from collections import defaultdict


class FallbacksFailed(Exception):
    pass


fallback_registry = defaultdict(list)



def fallback(id=None):
    def decorator(func):

        fallback_registry[id].append(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            functions = fallback_registry[id]
            for _func in functions:
                try:
                    return _func(*args, **kwargs)
                except Exception as e:
                    pass

            raise FallbacksFailed()

        return wrapper
    return decorator


