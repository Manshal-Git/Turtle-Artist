# import package and making object
import turtle

screen = turtle.Screen()

# method to draw ellipse
def draw_arc(rad):
    # rad --> radius for arc
    for i in range(1):
        turtle.circle(rad,75)
        turtle.circle(rad // 2, 75)

# Main screen size
screen.setup(500, 500)

# Set screen color
screen.bgcolor('black')

# orientation variation
val = 10

# Initial turtle speed and size
turtle.speed(100)
turtle.color("yellow")
turtle.pensize(3)

# loop for multiple arcs
for i in range(36*8):
    # oriented the ellipse at angle = -val
    turtle.seth(-val)

    # drawing shape method
    draw_arc(i * 1.2)

    # orientation change
    val += 100
    # keep the pen size thin after some rotation
    if i > 50:
        turtle.pensize(1)


# for hiding the turtle
turtle.hideturtle()
turtle.exitonclick()