total = int(input('Enter a number:'))

while True:
    b=int(input('Enter another number:'))
    total=total+b
    d=input('Do you want to add another number?(y/n)')
    if d=='y':
        continue
    else:
        break
print('Total number is',total,'.')