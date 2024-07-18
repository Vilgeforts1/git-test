from functools import update_wrapper
from typing import Any

class MathOperations:
    def __init__(self, function) -> None:
        self. func = function
        update_wrapper(self, function)

        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Работает декоратор-класс!")
        result = self.func(*args, **kwds)
        return result / len(args[0])

    

@MathOperations
def summ(l: list) -> int:
    print("Функция сум которая считает сумму элементов списка!")
    return sum(l)
    

print(summ([1, 2, 3]))