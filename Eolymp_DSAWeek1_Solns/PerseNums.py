num = int(input())
def ListOfNum(num):
    L = []
    while num != 0:
        x = num%10
        num = num//10
        L.append(x)
    return L
def Multiply(L):
    result = 1
    for i in L:
        result = result *i
    return result
L = ListOfNum(num) #L = [2,6,8]
result = 0
while len(L) > 1:
    result +=1
    x = Multiply(L)
    L = ListOfNum(x)
print(result)

number = int(input("enter number"))
product = 1
persistence = 0
print(number)
while number > 9:
    for digit in range(0, len(str(number))):
        product *= int(str(number)[digit])
    print(product)
    persistence += 1
    number = product
    product = 1
print("persistence:", persistence)