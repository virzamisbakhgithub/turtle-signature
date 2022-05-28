import turtle
an = turtle.Screen()
a = turtle.Turtle()

an.bgcolor("black")
a.color("red")
a.shape("circle")
a.pensize(8)
a.speed(10)

a.penup()
a.left(360)
a.bk(260)
a.pendown()


a.lt(200)
a.rt(50)
a.circle(-20,270)
a.fd(80)
a.rt(50)
a.lt(50)
a.circle(70,105)

a.rt(10)
a.lt(10)
a.circle(30,100)
a.fd(200)

a.rt(10)
a.lt(10)
a.circle(40,200)
a.fd(200)

a.rt(10)    #Small Wave
a.lt(10)
a.circle(10,160)
a.fd(80)

a.rt(10)
a.lt(10)
a.circle(10,200)
a.fd(80)

a.rt(10)
a.lt(10)
a.circle(10,160)
a.fd(80)

a.rt(10)
a.lt(10)
a.circle(10,200)
a.fd(80)

a.rt(10)
a.lt(10)
a.circle(10,160)
a.fd(80)

a.rt(10)
a.lt(10)
a.circle(10,200)
a.fd(80)    #Small Wave

a.rt(10)
a.lt(10)
a.circle(10,160)
a.fd(200)

a.rt(10)
a.lt(10)
a.circle(30,195)
a.fd(230)

a.rt(10)
a.lt(10)
a.circle(-10,290)
a.fd(30)

a.rt(10)
a.lt(10)
a.circle(10,50)

#---------------------------------
a.penup()
a.lt(60)
a.fd(200)
a.pendown()
#---------------------------------

a.lt(-40)
a.circle(-10,90)

#---------------------------------
a.penup()
a.lt(60)
a.fd(20)
a.pendown()
#---------------------------------

a.lt(70)
a.circle(-10,90)

#---------------------------------
a.penup()
a.left(30)
a.bk(400)
a.pendown()
#---------------------------------

a.rt(25)
a.circle(-950,25)
a.fd(20)

for x in range(180):
    a.lt(12)