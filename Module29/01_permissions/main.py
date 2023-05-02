from typing import Callable, Any, Optional
import functools

user_permissions = ['admin']


def check_permission(*, permission: str) -> Callable:
    """
    Функция принимает аргумент

    Arguments:
        permission (разрешения): чтобы выполнит функцию.

    И если уровень разрешения пользователя
    подходит под требования то функция выполняется в противном
    случае вызывается исключение
    """
    def decorator_permission(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Optional[Any]:
            try:
                if permission in user_permissions:
                    raise Exception("PermissionError: у пользователя недостаточно прав, "
                                    "чтобы выполнить функцию add_comment")

                return func(*args, **kwargs)
            except Exception as exc:
                print(exc)
        return wrapped
    return decorator_permission

@check_permission(permission='admin')
def delete_site():
    print('Удаляем сайт')

@check_permission(permission='user_1')
def add_comment():
    print('Добавляем комментарий')


if __name__ == "__main__":
    delete_site()
    add_comment()