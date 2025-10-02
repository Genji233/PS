import array
import random

a=array.array('i',[])
for i in range(5):
    b=random.randint(1,100)
    a.append(b)
b=array.array('i',[])
for i in range(3):
    c=int(input('Enter a number to be added:'))
    b.append(c)
a.extend(b)
for i in sorted(a):
    print(i)
