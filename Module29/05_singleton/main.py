import functools

class Singleton:
    """
    Декоратор для проектирования
    паттерана Singleton. Декоратор
    возвращает только один экземпляр
    """
    def __init__(self, cls):
        functools.update_wrapper(self, cls)
        self.__cls = cls
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = self.__cls(*args, **kwargs)

        return self.__instance

@Singleton
class Example:
    pass


if __name__ == "__main__":
    my_obj = Example()
    my_another_obj = Example()

    print(id(my_obj))
    print(id(my_another_obj))

    print(my_obj is my_another_obj)