def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        return ((-1) ** (-n + 1)) * f(-n)
    return f(n - 1) + f(n - 2)

def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)


fib(10)
f(-2)