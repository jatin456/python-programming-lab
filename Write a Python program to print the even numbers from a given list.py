list1=list(map(int,input("Enter elements space sepaarated: ").split()))
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
print()
print("List with even numbers")
print(list2)
        