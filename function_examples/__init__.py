#example 1
def a():
    print('inside a')


def b(x):
    print('inside b')
    return x


def c(y):
    print('inside c')
    return y()


print(a())
print(5+b(2))
print(c(a))

#example 2
def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4)
print(val)

def addition(a,b):
    x: int = a + b
    return x

print(addition(5,5))
