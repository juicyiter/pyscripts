def isBigger(a, b):
    if a > b:
        print(a, "is bigger than", b)
    elif a == b:
        print(a, "is equal to", b)
    else :
        print(a, "is smaller than", b)

m = int(input("Enter the first integer:"))
n = int(input("Enter the second integer:"))

isBigger(m, n)