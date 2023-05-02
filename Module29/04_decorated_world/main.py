from typing import Callable, Optional, Any
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор для обертки другого декоратора
    Сначала получает аргументы декоратора и
    возвращает другую обертку и получает функцию
    """
    @functools.wraps(decorator)
    def wrapped_get_args(*args, **kwargs) -> Callable:
        def wrapped_get_func(func: Callable) -> Optional[Any]:
            return decorator(func, *args, **kwargs)
        return wrapped_get_func
    return wrapped_get_args

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    print("Переданные арги и кварги в декоратор: {} {}".format(*args, **kwargs))

    @functools.wraps(func)
    def wrapped(*args2, **kwargs2) -> Optional[Any]:
        return func(*args2, **kwargs2)
    return wrapped

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


if __name__ == "__main__":
    decorated_function("Юзер", 101)