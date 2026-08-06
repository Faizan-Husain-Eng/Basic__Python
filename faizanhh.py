import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Text")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.penup()
pen.hideturtle()

text = "Faizan Husain Danila"

# Starting position
x = -250
y = 0

# Animate each letter
for letter in text:
    pen.goto(x, y)
    pen.write(letter, font=("Arial", 24, "bold"))
    x += 20
    time.sleep(0.1)

# Add glowing effect
colors = ["red", "yellow", "green", "blue", "purple"]

for i in range(5):
    pen.goto(-250, -50)
    pen.color(colors[i])
    pen.write(text, font=("Arial", 28, "bold"))
    time.sleep(0.3)
    pen.clear()

# Final display
pen.goto(-250, -50)
pen.color("white")
pen.write(text, font=("Arial", 28, "bold"))

turtle.done()