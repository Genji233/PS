nums=[123,345,456,789]
for i in nums:
    print(i)
a= int(input('Please enter a number:')) 
if a in nums:
    print(f'Position of {a} is '+str(nums.index(a)+1)+'.')  
else:
    print("That's not in the list.")