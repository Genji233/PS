a=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
b=int(input('Enter a row number:'))
print(a[b-1])
c=int(input('Enter a number to be added:'))
a[b-1].append(c)
print(a[b-1])