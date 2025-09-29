compnum=50
count=1
while True:
    a=int(input('Enter a number:'))
    if a==compnum:
        print('Well done, you took',count,'attempts!')
        break
    elif a<compnum:
        print('Too low! Guess again:')
        count+=1
        continue
    elif a>compnum:
        print('Too high! Guess again:')
        count+=1
        continue


