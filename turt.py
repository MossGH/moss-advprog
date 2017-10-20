import turtle
import time
window=turtle.Screen()

turt=turtle.Turtle()
turt.speed(0)
turt.ht()
for i in range (4):
    turt.fd(90)
    turt.lt(90)

turty=turtle.Turtle()
turty.ht()
turty.speed(0)
turty.lt(90)
turty.circle(90)

time.sleep(3)
window.bye()

window=turtle.Screen()

turt.speed(0)
turt.color("#00ff00")
turt.ht()
window.bgcolor("#000000")
for i in range (4):
    turt.fd(90)
    turt.lt(90)

turty=turtle.Turtle()
turty.ht()
turty.speed(0)
turty.lt(90)
turty.circle(90)

time.sleep(3)
window.bye()
