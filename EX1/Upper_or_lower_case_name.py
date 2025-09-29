fname = input("Enter your first name: ")
if len(fname) < 5 :
    sname = input("Enter your surname : ")
    fullname = fname.upper() + sname.upper()
    print(fullname)
else:
    print(fname.lower())