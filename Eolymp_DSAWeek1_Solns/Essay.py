times = int(input())
for i in range(times):
    num = int(input())
    if num%2 == 0:
        n = num//2
        print((n*n)*2)
    else:
        n = num//2
        print(n*(n+1)*2)
