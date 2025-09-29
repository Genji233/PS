a=input('Which direction do you want to count? (up/down)')
if a=='up':
    b=int(input('Please enter a top number:'))
    for i in range(1,b+1,1):
        print(i)
elif a=='down':
    b=int(input('Please enter a number below 20:'))
    for i in range(b,0,-1):
        print(i)
else:
    print('I do not understand.')