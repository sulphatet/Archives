num = int(input())
def fib(num):
    j = {0:0,1:1}
    if num <= 2:
        return 1
    elif num not in j:
        j[num] = fib(num-1)+fib(num-2)
        return j[num]
def fibo(num):
    if num ==0:
        return 0
    if num == 1:
        return 1
    return fibo(num-1) + fibo(num-2)
print(fibo(num+1))
