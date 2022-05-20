def voting(a):
    if a>=18:
        return "You are eligilible for voting"
    else:
        return "You are not eligilible for voting"
c=int(input("Enter your age:"))
d=voting(c)
print(d)

