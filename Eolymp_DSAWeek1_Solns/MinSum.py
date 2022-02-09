nums = input()
L = nums.split()
def Sum(a):
    sum = 0
    while a != 0:
        sum = sum + int(a%10)
        a = a//10
    return sum


a = int(L[0])
b = int(L[1])
min = 10**7
if b - a < 10:
    while a != b:
        x = Sum(a)
        a +=1
        if x < min:
            min = x
else:
    for i in range(10):
        x = Sum(a)
        a +=1
        if x < min:
            min = x
print(x)
