nums = input()
L = nums.split()
m = int(L[0])
n = int(L[1])
def gcd(m,n):
    if m == 0:
        return n
    a = max(m,n)
    b = min(m,n)
    if a %b == 0:
        return b
    else:
        return gcd(a,a%b)
print(gcd(m,n))
