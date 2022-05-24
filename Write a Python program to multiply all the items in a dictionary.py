dict={'a':10,'b':20,"c":30,"d":40}
list=[]
mul=1
for i in dict.values():
    list.append(i)
for i in list:
    mul=mul*i
print(mul)
