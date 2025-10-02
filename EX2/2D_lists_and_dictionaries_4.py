a=[]
for i in range(4):
    print('Please enter information for person',i+1)
    name=input('Please enter a name:')
    age=int(input('Please enter a age:'))
    size=input('Please enter a size:')
    a.append([name,age,size])
for i in a:
    print('Name:',i[0],',Age:',i[1])
b=int(input('Please enter a person number to be deleted:'))
del a[b-1]
for i in a:
    print('Name:',i[0],',Age:',i[1])