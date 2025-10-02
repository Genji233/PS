import array
import random

a=array.array('i',[])
for i in range(5):
    b=int(input('Enter a number to be added:'))
    a.append(b)
a=array.array('i',sorted(a))
for i in a:
    print(i)
c=int(input('Enter a number to be removed:'))
d=a.pop(a.index(c))
e=array.array('i')
e.append(d)
for i in a:
    print(i)
