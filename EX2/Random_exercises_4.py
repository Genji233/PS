import random

color_hints = {
    "green": "I bet you are GREEN with envy!",
    "blue": "Don’t feel BLUE about it.",
    "red": "Looks like you’re seeing RED after that one.",
    "yellow": "That guess was a bit YELLOW-bellied.",
    "gold": "Keep trying until you strike it GOLD!"
}
color=random.choice(list(color_hints.keys()))
a = input("What is my favorite color?")
while True:
    if a == color:
        print("Well done!")
        break
    else:
        a=input(color_hints[color]+'Please try again:')
        continue
