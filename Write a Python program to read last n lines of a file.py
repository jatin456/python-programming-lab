f=open("data.txt","r")
a=f.readlines()
n=int(input())
for i in (a[-n:]):
    print(i)
