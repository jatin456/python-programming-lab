a={'aman':1,'ayush':2,'jatin':3,'akash':4}
b=input("Which key you want to remove")
if b in a:
    del a[b]
    print(a)
else:
    print("Key not found")