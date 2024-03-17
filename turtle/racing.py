import turtle as tt
import random as rd


tt.t1 = tt.Turtle()
tt.t2 = tt.Turtle()
tt.t3 = tt.Turtle()
tt.t4 = tt.Turtle()
tt.t5 = tt.Turtle()
tt.t6 = tt.Turtle()

tt.t2.speed(0)

tt.t1.shape('turtle')
tt.t3.shape('turtle')
tt.t4.shape('turtle')
tt.t5.shape('turtle')
tt.t6.shape('turtle')

tt.t1.color('red')
tt.t3.color('orange')
tt.t4.color('yellow')
tt.t5.color('green')
tt.t6.color('blue')

Screen = tt.Screen()
Screen.setup(1500,700)
Screen.title('거북이 게임')
Screen.bgcolor('cyan')

tt.t2.penup()
tt.t2.goto(300,-300)
tt.t2.pendown()


tt.t2.left(90)
tt.t2.forward(600)
tt.t2.left(90)
tt.t2.forward(1000)
tt.t2.left(90)
tt.t2.forward(600)
tt.t2.left(90)
tt.t2.forward(1000)


tt.t1.penup()
tt.t1.goto(300,0)
tt.t3.penup()
tt.t3.goto(300,-100)
tt.t4.penup()
tt.t4.goto(300,100)
tt.t5.penup()
tt.t5.goto(300,-200)
tt.t6.penup()
tt.t6.goto(300,200)
tt.t1.left(180)
tt.t3.left(180)
tt.t4.left(180)
tt.t5.left(180)
tt.t6.left(180)
while True:
    if tt.t1.xcor() <= -700:
        tt.t1.left(180)
        print('1등!! 제임스 우승!!')
        tt.exitonclick()
        break
    elif tt.t3.xcor() <= -700:
        tt.t3.left(180)
        print('1등!! 디두 우승!!')
        tt.exitonclick()
        break
    elif tt.t4.xcor() <= -700:
        tt.t4.left(180)
        print('1등!! 쿠루스 우승!!')
        tt.exitonclick()
        break
    elif tt.t5.xcor() <= -700:
        tt.t5.left(180)
        print('1등!! 알렉스 우승!!')
        tt.exitonclick()
        break
    elif tt.t6.xcor() <= -700:
        tt.t6.left(180)
        print('1등!! 린 우승!!')
        tt.exitonclick()
        break
    
    tt.t1.forward(rd.randint(1,50))
    tt.t3.forward(rd.randint(1,50))
    tt.t4.forward(rd.randint(1,50))
    tt.t5.forward(rd.randint(1,50))
    tt.t6.forward(rd.randint(1,50))
