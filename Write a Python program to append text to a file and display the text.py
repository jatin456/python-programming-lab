f=open("gupta1.txt","a")
f.write("\n")
f.write("jatin mohan gupta")
f.write("jatin")
print("data saved")
f.close()
f=open("gupta1.txt","r")

print(f.read())