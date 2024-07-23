from turtle import Turtle, Screen
import time
import random

win = Screen()
t = Turtle()

rootwindow = win.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

win.title('Go For Boxes')
t.hideturtle()


def get_coordinates() -> tuple:
    x_loc: int = random.randint(-150, 250)
    y_loc = random.randint(-150, 250)
    return x_loc, y_loc


def get_pen_attr() -> list:
    pen_size = random.randint(1, 10)
    pen_color = random.choice(['yellow', 'black', 'orange', 'red', 'green', 'blue'])
    return [pen_size, pen_color]


while True:
    x, y = get_coordinates()
    size = random.randint(50, 350)
    pensize, color = get_pen_attr()
    t.penup()
    t.goto(x, y)
    t.pen(pencolor=color, pensize=pensize)
    t.pendown()
    time.sleep(0.1)
    for i in range(4):
        t.right(90)
        t.forward(size)
        time.sleep(0.1)

# t.screen.mainloop()
win.mainloop()
