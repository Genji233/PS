a=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
b=int(input('Enter a row number:'))
print(a[b-1])
c=int(input('Enter a column number:'))
print(a[b-1][c-1])
d=input('Do you want to change the number? (yes/no):')
if d=='yes':
    e=int(input('Enter a new number:'))
    a[b-1][c-1]=e
print(a)
