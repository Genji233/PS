f=[]

for i in range(3):
    a=input('Please add a name of your friend:')
    f.append(a)
while True:
    b=input('Do you want to add another friend?(y/n)')
    if b=='y':
        c=input('Please add a name of your friend:')
        f.append(c)
    elif b=='n':
        print(f'You have invited {len(f)} friends to your party.')
        break
    else:
        print('Please enter y or n.')
        continue

