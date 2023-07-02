"""
Decorator : are a very powerful and useful tool in Python since it allows programmers
to modify the behaviour of a function or class. Decorators allow us to wrap another
function in order to extend the behaviour of the wrapped function, without permanently
 modifying it. But before diving deep into decorators let us understand some concepts that 
 will come in handy in learning the decorators.
"""
def div(a,b):
    print(a/b)

def div_smart(fun):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    
    return inner

div1 = div_smart(div)
div1(10,20)