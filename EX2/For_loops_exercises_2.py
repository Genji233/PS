total=0
print('Please enter 5 numbers:')
for i in range(5):
    a=int(input())
    b=input('Do you want that number to be included?(y/n)')
    if b=='y':
        total=total+a
        print('Please continue:')
    else:
        print('Please continue:')
        continue
print('Total number is',total,'.')
    
