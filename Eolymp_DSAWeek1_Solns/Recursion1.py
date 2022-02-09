num = int(input())
def f(n):
    if n <= 0:
        return 0
    return f(n-1) + n
print(f(num))
