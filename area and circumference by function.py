def circumarea(r):
    return 3.14*r*r,2*3.14*r
a=int(input("Enter the radius of a circle:"))
c,d=circumarea(a)
print("Area of a circle:",c,"\nCircumference of circle",d)