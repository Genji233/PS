k=True
while k:
    letter = input('Please enter a letter:')
    if len(letter) != 1 or not letter.isalpha():
        print('Invalid input. Please enter a single alphabetic character.')
        continue
    letter = letter.lower()
    if letter in 'aeiou':
        print(letter, 'is a vowel.')
    elif letter == 'y':
        print(letter, 'is sometimes a vowel, sometimes a consonant.')
    else:
        print(letter, 'is a consonant.')
    k=False