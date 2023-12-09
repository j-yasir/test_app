import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cool Python Drawing")

pen = turtle.Turtle()
pen.speed(2)
pen.color("cyan")

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Draw the star
pen.penup()
pen.goto(-50, 0)
pen.pendown()

draw_star(100)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.mainloop()
