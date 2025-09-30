foods={}
for i in range(4):
    a=input('Enter one of your favourite food:')
    foods[i+1]=a
for k,v in foods.items():
    print(f'{k}-{v}')
b = int(input('Which food do you want to get rid of?Enter the number:'))
del foods[b]
n=1
food_s={}
for i in range(len(foods.keys())):    
    food_s[i+1]=list(foods.values())[i]
foods=food_s
for k,v in foods.items():
    print(f'{k}-{v}')
