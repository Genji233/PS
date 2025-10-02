import array
import random

a = array.array('f', [])
for i in range(5):
    b = round(random.uniform(10, 100),2)
    print(b)
    a.append(b)
while True:
    c=int(input('Enter a whole number between 2 and 5:'))
    if c in range(2,6):
        for i in a:
            print(round(i/c,2))
        break
    else:
        print('Please enter a whole number between 2 and 5.Try again:')
        continue
