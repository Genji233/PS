name = input('Enter your name:')
num = int(input('Enter a number:'))
if num<10:
    for time in range(num):
        print(name)
else:
    for i in range(3):
        print('Too high!')