import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
flower = turtle.Turtle()
flower.speed(5)

# Function to draw a petal
def draw_petal():
    flower.color("pink")
    flower.begin_fill()
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    flower.end_fill()

# Draw flower petals
for i in range(6):
    draw_petal()
    flower.right(60)

# Draw center
flower.penup()
flower.goto(0, -20)
flower.pendown()
flower.color("yellow")
flower.begin_fill()
flower.circle(20)
flower.end_fill()

# Draw stem
flower.penup()
flower.goto(0, -40)
flower.setheading(-90)
flower.pendown()
flower.color("green")
flower.forward(150)

turtle.done()