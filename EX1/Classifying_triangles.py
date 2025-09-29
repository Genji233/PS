a = int(input('Please enter the lengths of first side of triangles: '))
b = int(input('Please enter the lengths of second side of triangles: '))
c = int(input('Please enter the lengths of third side of triangles: '))
if a==b==c:
    print('The triangle is an equilateral triangle.')
elif a==b or a==c or b==c:
    print('The triangle is isosceles.')
else:
    print('The triangle is scalene.')





