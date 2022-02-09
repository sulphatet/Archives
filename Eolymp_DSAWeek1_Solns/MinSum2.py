nums = input()
L = nums.split()
a = int(L[0])
b = int(L[1])
x = (b - a) + 1
def numDigits(y):
    x = y
    result = 0
    while x != 0:
        result +=1
        x = x//10
    if y % 10 == 0:
        return result
    return result -1
print(numDigits(x))

