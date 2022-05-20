def isprime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    return "Prime" if c==2 else "Not prime"
e=int(input("Enter a number"))    
d=isprime(e)
print(d)
