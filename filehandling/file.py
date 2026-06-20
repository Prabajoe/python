# x create
# w write
# r read
# a update
# remove delete

import os

# file created
r=open("D:\Maarison\demo.txt","x")
r.close()

# file write
r=open("D:\Maarison\demo.txt","w")
r.write("Hello python")
r.close()

# file read
r=open("D:\Maarison\demo.txt","r")
print(r.read())
r.close()

# file update or append

r=open("D:\Maarison\demo.txt","a")
r.write(" hello java")
r.close()

# file delete
r=os.remove("D:\Maarison\demo.txt")

# file created with statement 
with open("D:\Maarison\demo.txt","w") as f:
    f.write("demo file handling is done with example")

