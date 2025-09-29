while True:
    a=input('''1) Square
    2) Triangle
    Enter a number:''')
    if a=='1':
        side_s=int(input('Enter the side length of the square: '))
        print('The area of the square is '+str(side_s*side_s)+'.')
        break
    elif a=='2':
        base_s=int(input('Enter the base length of the triangle: '))
        height_s=int(input('Enter the height length of the triangle: '))
        print('The area of the triangle is '+str((base_s*height_s)/2)+'.')
        break
    else :
        print('Please enter a number between 1 and 2.')
        continue