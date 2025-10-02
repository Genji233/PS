import array
import random

a=array.array('i',[])
for i in range(5):
    b=random.randint(1,100)
    a.append(b)
for i in a:
    print(i)