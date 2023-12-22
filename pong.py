#import os
import turtle

####################################################################################################
#       controls:
#       left player (player 1): Q, A              right player (player 2): up, down
###################################################################################################


# Init screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("Black")
screen.setup(width = 1155, height = 650)

# Init L paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("White")
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Init R paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("White")
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
right_paddle.penup()
right_paddle.goto(400, 0)

# Init ball
ball = turtle.Turtle()
ball.speed(45)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# init score
left_score = 0
right_score = 0

# score display
score_sketch = turtle.Turtle()
score_sketch.speed(0)
score_sketch.color("White")
score_sketch.penup()
score_sketch.hideturtle()
score_sketch.goto(0, 220)
score_sketch.write("0     0",  align = "center", font = ("Courier", 60, "bold"))


## making dotted line using 2 turtles
# from the top
dotted_line_sketch1 = turtle.Turtle()
dotted_line_sketch1.speed(0)
dotted_line_sketch1.color("White")
dotted_line_sketch1.penup()
dotted_line_sketch1.hideturtle()
dotted_line_sketch1.goto(0, 325)
dotted_line_sketch1.setheading(270)
dotted_line_sketch1.pendown()

# from the bottom
dotted_line_sketch2 = turtle.Turtle()
dotted_line_sketch2.speed(0)
dotted_line_sketch2.color("White")
dotted_line_sketch2.penup()
dotted_line_sketch2.hideturtle()
dotted_line_sketch2.goto(0, -325)
dotted_line_sketch2.setheading(90)
dotted_line_sketch2.pendown()

# sketching the divider
for _ in range(16):
    dotted_line_sketch1.forward(10)
    dotted_line_sketch2.forward(10)
    dotted_line_sketch1.penup()
    dotted_line_sketch2.penup()
    dotted_line_sketch1.forward(10)
    dotted_line_sketch2.forward(10)
    dotted_line_sketch1.pendown()
    dotted_line_sketch2.pendown()

dotted_line_sketch1.forward(10)
dotted_line_sketch1.penup()
dotted_line_sketch1.forward(10)
dotted_line_sketch1.pendown()
   
# functions for moving paddles vertically
def paddle_L_up():
    if left_paddle.ycor() < 260:    # check bounds
        left_paddle.sety(left_paddle.ycor() + 20) 
   
def paddle_L_down():
    if left_paddle.ycor() > -260:
        left_paddle.sety(left_paddle.ycor() - 20) 

def paddle_R_up():
    if right_paddle.ycor() < 260:
        right_paddle.sety(right_paddle.ycor() + 20)
 
def paddle_R_down():
    if right_paddle.ycor() > -260:
        right_paddle.sety(right_paddle.ycor() - 20)
   
# key binding 
screen.listen()
screen.onkeypress(paddle_L_up, "q")
screen.onkeypress(paddle_L_down, "a")
screen.onkeypress(paddle_R_up, "Up")
screen.onkeypress(paddle_R_down, "Down")

# init hit counter for ball speed increase
hit_counter = 1

while True:

    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # left and right borders (scored)
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_score += 1 
        score_sketch.clear()
        score_sketch.write("{}     {}".format(left_score, right_score), align = "center", font = ("Courier", 60, "bold"))
        hit_counter = 1

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_score += 1
        score_sketch.clear()
        score_sketch.write("{}     {}".format(left_score, right_score), align = "center", font = ("Courier", 60, "bold"))
        hit_counter = 1

    # Collision of ball and R/L paddles
    if (ball.xcor() > 375 and ball.xcor() < 385) and (ball.ycor() < right_paddle.ycor() + 60 and ball.ycor() > right_paddle.ycor() - 60):  
        ball.setx(375)
        ball.dx *= -1
        hit_counter +=1

    if (ball.xcor() < -375 and ball.xcor() > -385) and (ball.ycor() < left_paddle.ycor() + 60 and ball.ycor() > left_paddle.ycor() - 60):  
        ball.setx(-375)
        ball.dx *= -1
        hit_counter +=1

    # speedup
    if hit_counter%3 == 0:
        ball.dx *= 1.15
        hit_counter = 1
