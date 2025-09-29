polygon_names = {
    3: "Triangle",
    4: "Quadrilateral",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon"
}
sides = int(input('How many sides does the shape have?'))
if  3<=sides<=10 :
    print('Name of this shape is '+polygon_names[sides]+'.')
else:
    print('Please enter a number between 3 and 10.')

