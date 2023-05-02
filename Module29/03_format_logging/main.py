from datetime import datetime
from print_time import date
from typing import Optional, Callable, Any
import functools
import time

def timer(func: Callable) -> Callable:
    """
    Декоратор таймер выводить время
    работы функций
    """
    @functools.wraps(func)
    def wrapped_timer(*args, **kwargs) -> Optional[Any]:
        start = time.time()
        result = func(*args, **kwargs)
        print("- Завершение '{name}', время работы = {time}s ".format(
            name=func.__qualname__,
            time=time.time() - start
            ))
        return result
    return wrapped_timer

def log_method_with_time(func: Optional[Callable] = None, *, create_time: str = date(datetime.now())) -> Callable:
    """
    Декоратор для логирования.
    Выводит время переданное аргументом
    """
    def log_method(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Optional[Any]:
            print("- Запускается '{name}'. Дата и время запуска: {date}".format(
                name=func.__qualname__,
                date=create_time
            ))

            return func(*args, **kwargs)
        return wrapped

    if func is None:
        return log_method
    return log_method(func)


def log_methods_with_time(create_time: str):
    """
    Декоратор для класса. Оборачивает все методы
    класса вручную указанными декораторами
    Это timer() и log_method_with_time()

    :param create_time: Время создания класса
    """
    def log_methods(cls):
        for attribute in dir(cls):
            if attribute.startswith("__"):
                continue

            method = getattr(cls, attribute)
            if hasattr(method, "__call__"):
                # Тут внутри setattr(.., декораторы для обертки метода)
                setattr(cls, attribute, timer(log_method_with_time(method, create_time=create_time)))

        return cls
    return log_methods


@log_methods_with_time(date(datetime.now()))
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods_with_time(date(datetime.now()))
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


if __name__ == "__main__":
    my_obj = B()
    my_obj.test_sum_1()
    time.sleep(1)
    my_obj.test_sum_2()
