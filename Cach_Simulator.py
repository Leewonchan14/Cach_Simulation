import sys

#python Cach_Simulator.py

args = sys.argv
for i in args:
    print(i)

f = open("read01.trace","r")
data = f.read()
f.close()
print(data)