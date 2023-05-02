from typing import Callable, Union

import main

def get(HTTP_user: str) -> Union[Callable, None]:
    func, HTTP = main.example

    if HTTP == HTTP_user:
        return func