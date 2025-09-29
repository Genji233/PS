import random

num=random.randint(1,5)
a=int(input('Please guess the number: (1-5)'))
if num==a:
    print('Well done!')
else:
    if num<a:
        b=int(input('Too high!Try again:'))
    if num>a:
        b=int(input('Too low!Try again:'))
    if num==b:
        print('Correct.')
    else:
        print('You lose.')