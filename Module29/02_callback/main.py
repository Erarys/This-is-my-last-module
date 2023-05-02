from typing import Any, Callable, Tuple
import functools

import app


def callback(*, HTTP_server: str) -> Callable:
    """
    Декоратор, заменяет функцию с кортежом
    """
    def decorator_callback(func: Callable) -> Tuple[Callable, str]:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> str | Any:
            return func(*args, **kwargs)

        return wrapped, HTTP_server
    return decorator_callback


@callback(HTTP_server='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


if __name__ == "__main__":
    route = app.get('//')
    if route:
        response = route()
        print('Ответ:', response)
    else:
        print('Такого пути нет')