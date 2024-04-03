from turtle import Turtle, Screen

screen = Screen()
paddle = Turtle()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")



paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(x=350, y=0)



game_on = True
while game_on:
    screen.update()



screen.exitonclick()



