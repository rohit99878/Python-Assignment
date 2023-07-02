"""
Generator : A generator-function is defined like a normal function, but whenever
it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.
"""

def topten():
    yield 5
    yield 6
values = topten()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)