import pgzrun
import random

HEIGHT=300
WIDTH=300
TITLE="RECTANGLE"

def draw():
    screen.fill("black")
    #rectangles width and height

    width=WIDTH
    height=HEIGHT-200
    r=255
    g=0
    b=random.randint(120,255)

    for i in range(20):
        myRect=Rect((0,0),(width,height))
        myRect.center=150,150
        screen.draw.rect(myRect,(r,g,b))
        width=width-10
        height=height+10
        r=r-10
        g=g+10     
pgzrun.go()