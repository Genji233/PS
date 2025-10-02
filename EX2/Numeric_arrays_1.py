import array

l = []
for i in range(5):
    a=int(input('Enter 5 numbers to create a list:'))
    l.append(a)
num=array.array( 'i', [])
num.extend(l)
print(num)
num.reverse()
print(num)

