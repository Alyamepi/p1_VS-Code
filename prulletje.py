print("Hello")
def func(x):
    print ("enter "+str(x)+" numbers")
    num = list(range(x))
    for i in range(x):
        num[i]=int(input("enter a number: ...>"))
    return sum(num)
print(func(3))