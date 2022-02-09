x = input()
X = x.split()
def f(a,b):
    m = min(a,b)
    n = max(a,b)
    if m == 0:
        return 1
    if m == n:
        return 1
    if m < n and 0 < m:
        return f(m-1,n-1)+f(m,n-1)
X[0] = int(X[0])
X[1] = int(X[1])
print(f(X[0],X[1]))

