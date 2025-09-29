a = input("Enter a word: ").lower()
letter = a[0]
if letter not in "aeiou":
    print(a[1:]+a[0]+'ay')
else :
    print(a + 'way')
