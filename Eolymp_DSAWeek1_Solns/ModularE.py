nums = input()
x = nums.split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
result = a%c
for i in range(b-1):
    result = (result * (a%c))%c
print(result)
