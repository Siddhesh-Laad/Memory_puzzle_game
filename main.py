from random import shuffle
from turtle import *
from freegames import path

# Build a platform with 64 frames
car = path("car.gif")
tiles = list(range(32)) * 2
state = {"mark": None}
hide = [True] * 64

# Create a function to draw the squares
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    # Set the colors of the squares
    color("black", "white")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state["mark"]

    # Show on screen if two selected numbers are equal
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state["mark"] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state["mark"] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state["mark"]

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color("black")
        write(tiles[mark], font=("Arial", 30, "normal"))

    update()
    ontimer(draw, 500)  # Increase the delay to 500 milliseconds

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
