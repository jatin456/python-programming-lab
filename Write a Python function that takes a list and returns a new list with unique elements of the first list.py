list1=list(map(int,input("Enter elements of lists space separated: ").split()))
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)