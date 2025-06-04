"""
Stub module for hypothesis to support tests without installing hypothesis.
"""


class HealthCheck:
    function_scoped_fixture = None


def example(*args, **kwargs):
    def decorator(f):
        return f

    return decorator


def settings(*args, **kwargs):
    def decorator(f):
        return f

    return decorator


def given(**kwargs):
    def decorator(f):
        def wrapper(*args, **other_kwargs):
            if kwargs:
                key, values = next(iter(kwargs.items()))
                for v in values:
                    f(*args, **{**other_kwargs, key: v})
            else:
                f(*args, **other_kwargs)

        return wrapper

    return decorator
