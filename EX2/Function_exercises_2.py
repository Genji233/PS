name_list=["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "John", "Kevin"]
while True:
    print('''Select a function:
    1)Add a name
    2)Delete a name
    3)Change a name
    4)List all names
    5)Exit''')
    choice=int(input())
    if choice==1:
        name=input("Enter the name to add: ")
        name_list.append(name)
        print(name,'has been added.')
        continue
    elif choice==2:
        for i,names in enumerate(name_list, start=1):
            print(str(i)+'. '+names)
        num=int(input("Enter the number of the name to delete: "))
        a=input(f"Are you sure you want to delete the name {name_list[num-1]} ? (y/n): ")
        if a=='y':
            b = name_list[num-1]
            del name_list[num-1]
            print(b,'has been deleted.')
            continue
        elif a=='n':
            continue
    elif choice==3:
        for i,names in enumerate(name_list, start=1):
            print(str(i)+'. '+names)
        num=int(input("Enter the number of the name to change: "))
        b=input(f"Are you sure you want to change the name {name_list[num-1]} ? (y/n): ")
        if b=='y':
            c=name_list[num-1]
            name_list[num-1]=input("Enter the new name: ")
            print(c,'has been changed to',name_list[num-1]+'.')
            continue
        elif b=='n':
            continue
    elif choice==4:
        for i,names in enumerate(name_list, start=1):
            print(str(i)+'. '+names)
            continue
    elif choice==5:
        print("Thank you for using!")
        break
    else:
        print("Invalid input.Please try num 1-5.")
        continue