def evenodd(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input("Enter a number:"))
d=evenodd(a)
print(d)