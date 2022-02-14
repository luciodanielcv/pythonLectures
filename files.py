import os

f = open ("text.txt", "a")

f.write("Adding text to the file")
f.close()

f = open ("text.txt")

print("Print in for loop")
for x in f:
    print(x)

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The files does not exist")

