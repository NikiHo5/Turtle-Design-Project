#Nickolas Ho
#function files



def polygon(t,s,d):
    a = 360/s
    for times in range(s):
        t.forward(d)
        t.right(a)


def polygonFill(t,s,d,c):
    a = 360/s
    t.color(c)
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)


def flowerfill(t,d,x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.begin_fill()
    
    for times in range(5):
    
        t.left(5)
        t.forward(d)#
        t.left(20)
        t.forward(d)#
        t.left(10)
        t.forward(d)#
        for times in range(13):
            t.forward(d)#
            t.left(5)
        for times in range(7):
            t.forward(d)#
            t.right(2)
        t.left(100)
        for times in range(7):
            t.forward(d)#
            t.right(2)
        for times in range(13):
            t.forward(d)#
            t.left(5)
        t.left(5)
        t.forward(d)#
        t.left(20)
        t.forward(d)#
        t.left(10)
        t.forward(d)#
        t.right(200)

    t.end_fill()
 
def flower(t,d,x,y):
    jump(t,x,y)
    for times in range(5):
        t.left(5)
        t.forward(d)#
        t.left(20)
        t.forward(d)#
        t.left(10)
        t.forward(d)#
        for times in range(13):
            t.forward(d)#
            t.left(5)
        for times in range(7):
            t.forward(d)#
            t.right(2)
        t.left(100)
        for times in range(7):
            t.forward(d)#
            t.right(2)
        for times in range(13):
            t.forward(d)#
            t.left(5)
        t.left(5)
        t.forward(d)#
        t.left(20)
        t.forward(d)#
        t.left(10)
        t.forward(d)#
        t.right(200)



def lumps(t,x,y,c1,c2):
    t.color(c1,c2,0)
    t.width(15)
    jump(t,x,y)#
    for times in range(8):
        t.forward(8)
        t.right(9)
    t.left(65)
    for times in range(11):
        t.forward(9)
        t.right(9)
    t.left(65)
    for times in range(8):
        t.forward(9)
        t.right(9)
    t.right(247)
