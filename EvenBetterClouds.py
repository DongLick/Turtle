from turtle import*
from random import*

color('white')
fillcolor('white')
bgcolor('skyblue')
pensize(2)
speed(100)
penup()
cloudDone = False

def semiCircle(size, arc):
    pendown()
    for i in range(0, arc):
        forward(size)
        left(9)

def homeCheck(x, y):
    global cloudDone
    if ycor() < y or ycor() < y + 30:
        goto(x, y)
        end_fill()
        cloudDone = True

def adjustTurn():
    randTurn = randint(160, 270)
    if heading() >= 360 or heading() <= 180:
        left(randint(45, 225))
        
    left(randTurn)
    # if hdng >= 0 and hdng <= 90:
    #     left(randTurn * randint(9, 11))
    # if hdng > 90 and hdng <= 180:
    #     left(randTurn * randint(2, 3))
    # if hdng > 180 and hdng <=270:
    #     left(randTurn * randint(2, 4))
    # if hdng > 270 and hdng < 0:
    #     left(randTurn * randint(3, 5))

def cloud(x, y):
    up()
    goto(x, y)
    setheading(randint(-30, 30))
    down()
    global cloudDone
    cloudDone = False
    begin_fill()
    while cloudDone == False:
        size = randint(2, 11)
        semiCircle(size, randint(19, 21))
        adjustTurn()
        homeCheck(x, y)

cloud(0, 0)
for i in range(0, 10):
    x = randint(-300, 300)
    y = randint(-250, 250)
    cloud(x, y)

exitonclick()