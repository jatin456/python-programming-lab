f=open("data.txt","r")
a=f.read().split()
m=len(max(a,key=len))
for i in a:
    if len(i)==m:
        print(i)
