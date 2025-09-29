import random
import turtle
colors=["red", "green", "blue", "yellow","orange", "purple"]
t = turtle.Turtle()
for i in range(random.randint(50,100)):
    t.color(random.choice(colors))
    t.forward(random.randint(1,100))
    t.right(random.uniform(-100,100))