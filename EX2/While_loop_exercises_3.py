num=10
while True:
    if num !=0:
        print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall,how many green bottles will be hanging on the wall?")
        a=int(input())
        if a==num-1:
            num-=1
            continue
        else:
            print('No, try again.')
    else: 
        print('There are no more green bottles hanging on the wall.')
        break