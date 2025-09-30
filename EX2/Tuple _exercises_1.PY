countries=('Canada', 'Brazil', 'Japan','Egypt', 'Australia')
for country in countries:
    print(country)
c= input('Enter tha name of one of these country.')
print(f'The index of this country is {countries.index(c)+1}.')
d= int(input('Enter an index of a country:'))
print(f'The country is {countries[d-1]}.')