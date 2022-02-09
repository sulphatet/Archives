num = int(input())
for i in range(num):
    nums = input()
    L = nums.split()
    a = int(L[0])
    b = int(L[1])
    max = b
    while b!=1:
        if b%2 == 0:
            b = int(b/2)
        else:
            b = (b*3)+1
        if b > max:
            max = b
    print(str(a) + ' '+ str(max))

