nums = input()
L = nums.split()
TelDist = 0
x = int(L[0])
y = int(L[1])
a = int(L[2])
b = int(L[3])
if abs(x-a) < abs(x-b):
    start = a
    end = b
else:
    start = b
    end = a
TelDist += abs(start-x)
TelDist += abs(end-y)
if TelDist < abs(x-y):
    print(TelDist)
else:
    print(abs(x-y))
