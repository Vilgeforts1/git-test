# float iterator
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def foo(l):
    for sublist in l:
        yield from sublist
        
        
        
for i in foo([[1, 2, 3], [5, 6, 7]]):
    print(i)