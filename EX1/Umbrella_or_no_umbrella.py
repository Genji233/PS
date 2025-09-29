a = input('Is it raining? (yes/no): ').lower()
if a == 'yes':
    b=input('Is it windy? (yes/no): ').lower()
    if b == 'yes':
        print('No umbrella, too windy.')
    else:
        print('Take an umbrella.')
else:
    print('No umbrella needed.')