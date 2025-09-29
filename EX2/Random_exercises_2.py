import random

c=random.choice(['h','t'])
a=input('Head or Tail?(h/t)')
if a==c:
    print('You win.')
elif a!=c:
    print('You lose.')
if c=='h':
    print('I chose head.')
else:
    print('I chose tail.')