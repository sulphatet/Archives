nums = input()
L = nums.split()
x = int(L[0])
n = int(L[1])
y = x**n
if y < 10**18:
    print(y)
