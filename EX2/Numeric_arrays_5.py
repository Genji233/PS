import array
import random

a = array.array('i', [])
for i in range(5):
    b = random.randint(1, 100)
    print(b)
    a.append(b)
while True:
    c = int(input('Enter a number to be indexed:'))
    if c in a:
        print(f'The position is {a.index(c) + 1}.')
        break
    else:
        print('The number is not in the list.')
        continue
