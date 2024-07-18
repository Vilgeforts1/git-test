from functools import wraps
from math import acos

class Arg:
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(vec1, vec2):
            mod_vec1 = sum([el ** 2 for el in vec1]) ** 0.5
            mod_vec2 = sum([el ** 2 for el in vec2]) ** 0.5
            dot_prod = func(vec1, vec2)
            return acos(dot_prod / (mod_vec1 * mod_vec2))
        return wrapper



@Arg()
def dot_product(vec1: tuple, vec2: tuple) -> int:
    result = 0
    for x, y in zip(vec1, vec2):
        result += x * y
    return result


# dot_product = Arg()(dot_product)
# OR
# decor = Arg()
# dot_product = decor(dot_product)
res = dot_product((0, 1), (1, 0))


print(f'Угол между векторами равен {res}')