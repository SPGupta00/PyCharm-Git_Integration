def factorial(l):
    fact = 1
    for i in range(1, l + 1):
        faco *= i
    return fact

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

l = int(input("Enter a number"))
n = int(input("Enter a number"))
print(factorial(l))
print(factorial(n))