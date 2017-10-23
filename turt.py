import turtle
import time
window=turtle.Screen()

turt=turtle.Turtle()
turt.speed(0)
turt.ht()
turt.rt(45)
for i in range (4):
    turt.fd(90)
    turt.lt(90)

turty=turtle.Turtle()
turty.ht()
turty.speed(0)
turty.lt(90)
turty.circle(90)

time.sleep(1)

window.bgcolor("#000000")
turt.color("#00ff00")

turt.rt(15)
for i in range (6):
    turt.fd(90)
    turt.lt(60)

turty.color("#00ff00")
turty.circle(90)

time.sleep(1)

turt.clear()
turty.clear()
##for i in range (360):
##    turt.rt(1)
##    turt.fd(1)
##    for i in range (4):
##        turt.fd(90)
##        turt.lt(90)

##time.sleep(1)

turt.seth(0)
turt.fd(100)
turt.rt(90)
turt.fd(20)
turt.rt(90)
turt.fd(40)
turt.lt(90)
turt.fd(80)
turt.lt(180)
turt.circle(30,-180)
turt.lt(90)
turt.fd(10)
turt.rt(90)
turt.circle(20,180)

window.exitonclick()
