num = int(input())
x = 0
if num == 0:
    print(1)
    exit()
while num != 0:
    x +=1
    num = num//10
print(x)
