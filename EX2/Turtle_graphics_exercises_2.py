import random
import turtle
colors=["red", "green", "blue", "yellow","orange", "purple"]
t = turtle.Turtle()
for i in range(8):
    t.color(random.choice(colors))
    t.forward(100)
    t.right(45)