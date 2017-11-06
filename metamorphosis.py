#Nickolas Ho
import turtle######WARNING#######TAKES 30 MIN TO LOAD
logan = turtle.Turtle()#background
bob = turtle.Turtle()#flower
andy = turtle.Turtle()#butterfly
tom = turtle.Turtle()#bottom wing
kelly = turtle.Turtle()#designs
luke = turtle.Turtle()#feet
logan.hideturtle()
bob.hideturtle()
andy.hideturtle()
tom.hideturtle()
kelly.hideturtle()
luke.hideturtle()
turtle.colormode(255)
from myFunctions import*
logan.speed(1000)
bob.speed(1000000)
andy.speed(10000)
tom.speed(100000)
kelly.speed(1000000)
luke.speed(1000000)
logan.width(20)
bob.width(7)
andy.width(15)
tom.width(4)
kelly.width(15)
luke.width(15)


for times in range(225):#
    logan.color(240-times,255,240-times)
    logan.circle(times*5)
    jump(logan,0,0-times*5)
for times in range(20):
    bob.color(190+3*times,100+5*times,255-times)
    flower(bob,8-times*.2,-2.5*times,-5)
bob.left(180)
for times in range(20):
    bob.color(120+2*times,120+times*5,235+times)
    flower(bob,7-times*.2,-208+3*times,-25)
bob.left(48)#was 170
for times in range(20):
    bob.color(80+6*times,140+times,235+times)
    flower(bob,6-times*.2,-165+2*times,-75+2*times)
bob.left(170)
bob.left(235)
for times in range(20):
    bob.color(195+3*times,82+3*times,255-5*times)#was215
    flower(bob,5-times*.2,-103,-65+2*times)
bob.left(60)     
jump(bob,-112,-10)
for times in range(101):
    bob.width(3)
    bob.color(255,255-times,155+times)
    bob.right(360/5)
    bob.circle(times/5)
jump(andy,70,15)
andy.left(130)
andy.forward(200)
andy.width(6)
andy.left(10)
andy.forward(90)
andy.width(8)
andy.circle(4)
jump(andy,-60,170)
andy.right(20)
andy.width(6)
andy.forward(90)
andy.width(8)
andy.circle(4)



###Back###



jump(andy,-30,158)
andy.begin_fill()
andy.left(2)
andy.color(196,117,39)
andy.right(20)
andy.forward(10)
for times in range(4):
    andy.right(5)
    andy.forward(10)
for times in range(2):
    andy.forward(10)
    andy.right(5)
andy.forward(20)
for times in range(4):
    andy.forward(10)
    andy.right(4)
for times in range(12):
    andy.forward(10)
    andy.right(2)
for times in range(5):
    andy.forward(10)
    andy.right(10)

for times in range(7):
    andy.forward(8)
    andy.right(9)

andy.left(70)
for times in range(12):
    andy.forward(9)
    andy.right(9)
andy.left(70)
for times in range(7):
    andy.forward(9)
    andy.right(9)
for times in range(3):
    andy.forward(7)
    andy.right(10)

andy.right(160)
andy.end_fill()

andy.begin_fill()
jump(andy,36,105)
for times in range(19):
    andy.forward(10)
    andy.right(3.4)
for times in range(10):
    andy.right(4)
    andy.forward(6)
andy.left(65)
andy.forward(100)
andy.left(190)
andy.forward(100)
andy.left(65)
for times in range(10):
    andy.right(4)
    andy.forward(6)
for times in range(15):
    andy.forward(10)
    andy.right(3.85)

for times in range(4):
    andy.forward(8)
    andy.right(6)
andy.right(280)


andy.end_fill()


######FRONT###########
andy.pendown()#:(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
jump(andy,60,365)###
andy.color(180,74,24)
andy.begin_fill()
andy.right(197)

for times in range(5):
    andy.forward(10)
    andy.right(10)

for times in range(7):
    andy.forward(8)
    andy.right(9)

andy.left(70)
for times in range(12):
    andy.forward(9)
    andy.right(9)
andy.left(70)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.forward(9)
andy.right(70)
andy.forward(15)
andy.left(10)
andy.forward(15)
andy.left(10)
andy.forward(8)
andy.right(125)
for times in range(9):
    andy.forward(8)
    andy.left(9)

andy.right(65)
for times in range(11):
    andy.forward(9)
    andy.left(9)
andy.right(65)
for times in range(7):
    andy.forward(9)
    andy.left(9)
andy.goto(60,365)
andy.end_fill()###
jump(andy,53,360)
andy.left(40)
andy.forward(10)
andy.left(140)
#########  color r+1  g +1
###########
andy.color(200,100,0)
andy.width(15)
jump(andy,44,350)
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(202,101,0)
andy.width(15)
jump(andy,40,347)
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(204,103,0)
andy.width(15)
jump(andy,37,344)
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(206,105,0)
andy.width(15)
jump(andy,35,342)
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(208,105,0)######5
andy.width(15)
jump(andy,32,340)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)

andy.color(210,107,0)#
andy.width(15)
jump(andy,29,337)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(214,109,0)#
andy.width(15)
jump(andy,26,336)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(215,111,0)#
andy.width(15)
jump(andy,23,335)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(217,113,0)#
andy.width(15)
jump(andy,22,334)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)

andy.color(219,114,0)#
andy.width(15)
jump(andy,21,332)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(221,115,0)####10
andy.width(15)
jump(andy,20,331)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(223,116,0)#
andy.width(15)
jump(andy,19,329)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(223,116,0)#
andy.width(15)
jump(andy,16,328)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)

andy.color(225,117,0)#
andy.width(15)
jump(andy,15,327)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)

andy.color(227,118,0)#
andy.width(15)
jump(andy,13,326)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(228,120,0)#####15
andy.width(15)
jump(andy,11.5,324)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)


andy.color(230,121,0)#
andy.width(15)
jump(andy,9,321)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(232,123,0)#
andy.width(15)
jump(andy,7,319)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(234,125,0)#
andy.width(15)
jump(andy,8,318.5)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(236,127,0)#
andy.width(15)
jump(andy,6,317)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)



andy.color(238,129,0)######20
andy.width(15)
jump(andy,3,315)#
for times in range(8):
    andy.forward(8)
    andy.right(9)
andy.left(65)
for times in range(11):
    andy.forward(9)
    andy.right(9)
andy.left(65)
for times in range(8):
    andy.forward(9)
    andy.right(9)
andy.right(247)

lumps(andy,2,314,239,131)#

lumps(andy,0,311,240,132)#

lumps(andy,-2,308,240,133)#

lumps(andy,-4,305,240,135)#

lumps(andy,-6,302,240,137)######25

lumps(andy,-7,299,240,138)#

lumps(andy,-10,296,240,139)#

lumps(andy,-13,293,242,140)#

lumps(andy,-16,290,244,142)#

lumps(andy,-18,287,246,142)######30

lumps(andy,-20,284,247,144)#

lumps(andy,-23,281,245,145)#

lumps(andy,-25,278,245,146)#

lumps(andy,-27,275,245,148)#

lumps(andy,-29,271,245,150)########35

lumps(andy,-30,269,246,151)#

lumps(andy,-31,267,246,153)#

lumps(andy,-32,265,247,154)#

lumps(andy,-33,263,247,156)#

lumps(andy,-34,260,248,158)#######40

lumps(andy,-35,258,248,160)#

lumps(andy,-36,256,249,162)#

lumps(andy,-37,253,249,164)#

lumps(andy,-38,250,250,167)#

lumps(andy,-38,248,250,170)#######45

lumps(andy,-39,246,252,172)#

lumps(andy,-39,244,252,175)#

lumps(andy,-40,242,253,176)#

lumps(andy,-40,240,253,178)#

lumps(andy,-41,237,253,180)#####50

lumps(andy,-41,235,253,181)#

lumps(andy,-42,233,253,182)#

lumps(andy,-42,231,253,183)#

lumps(andy,-43,228,253,185)#

lumps(andy,-43,226,253,186)#######55

lumps(andy,-43,224,253,185)#

lumps(andy,-43,222,253,185)#

lumps(andy,-43,220,253,185)#

lumps(andy,-44,218,253,185)#

lumps(andy,-44,216,253,185)######60

lumps(andy,-44,214,253,185)#

lumps(andy,-45,212,253,185)#

lumps(andy,-45,210,253,185)#

lumps(andy,-45,208,253,185)#

lumps(andy,-46,206,253,185)#######65

lumps(andy,-46,204,253,185)#

lumps(andy,-46,202,253,185)#

lumps(andy,-46,200,253,185)#
andy.width(24)
lumps(andy,-47,194,253,185)#
andy.begin_fill()
lumps(andy,-47,183,253,185)#########70

andy.goto(-23,147)
andy.left(129)

andy.forward(40)

andy.end_fill()

########
##########
jump(tom,12,97)
tom.right(185)
tom.color(238,137,55)
tom.begin_fill()
tom.right(113)
for times in range(21):
    tom.forward(10)
    tom.right(3.4)
for times in range(10):
    tom.right(4)
    tom.forward(6)
tom.left(65)
tom.forward(100)
tom.left(190)
tom.forward(100)
tom.left(65)
for times in range(10):
    tom.right(4)
    tom.forward(6)
for times in range(18):
    tom.forward(10)
    tom.right(3)
tom.right(301)
tom.end_fill()


jump(kelly,70,15)
kelly.left(130)
kelly.forward(200)
kelly.width(3)
jump(kelly,147,345)#######first#####
kelly.left(47)
for times in range(9):
    kelly.left(5)
    kelly.forward(6)
kelly.right(12)
for times in range(23):
    kelly.forward(12)
    kelly.left(3.5)
kelly.right(120)
jump(kelly,200,263)#######second#####
for times in range(9):
    kelly.left(5)
    kelly.forward(6)
kelly.right(12)
for times in range(9):
    kelly.forward(12)
    kelly.left(6)
kelly.forward(1)

kelly.begin_fill()#####second layer
kelly.color(255,153,51)######CHANGE####
kelly.right(193)
jump(kelly,14,82)
for times in range(20):
    kelly.forward(10)
    kelly.right(3.4)
for times in range(10):
    kelly.right(4)
    kelly.forward(6)
kelly.right(110)######
kelly.forward(100)
kelly.right(190)#CHANGE
kelly.forward(100)
kelly.right(110)#####
for times in range(10):
    kelly.right(4)
    kelly.forward(6)
for times in range(16):
    kelly.forward(10)
    kelly.right(3)
kelly.goto(14,82)
kelly.end_fill()


jump(kelly,55,70)
kelly.begin_fill()
kelly.goto(60,80)
kelly.color(232,138,44)#####CHANGE######
kelly.right(115)
for times in range(4):
    kelly.forward(10)
    kelly.right(2)
for times in range(15):
    kelly.forward(8)
    kelly.right(4)
for times in range(3):
    kelly.forward(5)
    kelly.right(6)
kelly.right(135)
for times in range(9):
    kelly.forward(10)
    kelly.left(5)
kelly.left(105)
for times in range(9):
    kelly.forward(10)
    kelly.left(5)
kelly.right(148)
for times in range(3):
    kelly.forward(5)
    kelly.right(6)
for times in range(15):
    kelly.forward(8)
    kelly.right(4)
for times in range(4):
    kelly.forward(10)
    kelly.right(2)

kelly.end_fill()




jump(luke,70,15)
luke.left(130)
luke.forward(200)
luke.width(3)
jump(luke,3,104)
luke.left(133)
luke.forward(100)
luke.right(50)
luke.forward(25)
jump(luke,25,65)
luke.left(5)
luke.forward(75)
luke.left(16)
luke.forward(20)
jump(luke,70,15)

turtle.done()
