import turtle
import math

sun = turtle.Turtle() 
sun.color("yellow")          #设置太阳的颜色
sun.shape("circle")          #设置太阳的形状
sun.up()
sun.setx(-1)

saturn = turtle.Turtle()
saturn.pensize(1)
saturn.color("blue")
saturn.shape("circle")
saturn.speed(0)
saturn.up()
saturn.setx(300)             #让土星初始位置到达（300,0）
saturn.down()

jupiter = turtle.Turtle()
jupiter.pensize(1)
jupiter.color("orange")
jupiter.shape("circle")
jupiter.speed(0)
jupiter.up()
jupiter.setx(250)
jupiter.down()

mars = turtle.Turtle()
mars.pensize(1)
mars.shape("circle")
mars.speed(0)
mars.up()
mars.setx(200)
mars.down()

earth = turtle.Turtle()
earth.pensize(1)
earth.color("red")
earth.shape("circle")
earth.speed(0)
earth.up()
earth.setx(150)
earth.down()

venus = turtle.Turtle()
venus.pensize(1)
venus.color("green")
venus.shape("circle")
venus.speed(0)
venus.up()
venus.setx(100)
venus.down()

mercury = turtle.Turtle()
mercury.pensize(1)
mercury.color("blue")
mercury.shape("circle")
mercury.speed(0)
mercury.up()
mercury.setx(50)
mercury.speed(0)
mercury.down()

def r(x):                        #用此函数将弧度制转化为角度制。
    y = x * math.pi / 180  
    return y
def b(a):                        #用此函数求出椭圆的半短轴长。
    b = (a ** 2 - 1) ** 0.5
    return b

while True:
    for i in range(360):
        saturn.goto(300 * math.cos(r(i)), b(300) * math.sin(r(i)))
        jupiter.goto(250 * math.cos(r(i * 2)), b(250) * math.sin(r(i * 2)))
        mars.goto(200 * math.cos(r(i * 3)), b(200) * math.sin(r(i * 3)))
        earth.goto(150 * math.cos(r(i * 4)), b(150) * math.sin(r(i * 4)))
        venus.goto(100 * math.cos(r(i * 5)), b(100) * math.sin(r(i * 5)))
        mercury.goto(50 * math.cos(r(i * 6)), b(50) * math.sin(r(i * 6)))
#用参数方程表示椭圆，各行星有不同的角速度。

