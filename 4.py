def fib_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = fib_rec(n-1)
        b = fib_rec(n-2)
        return a+b

print(fib_rec(5))