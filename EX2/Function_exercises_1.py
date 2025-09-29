def enter_num():
    num=int(input('Please enter a number:'))
    return num

def count(a:int):
    for i in range(1,a+1):
        print(i)
    return 0
count(enter_num())