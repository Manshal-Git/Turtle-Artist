# import package and making object
import turtle

screen = turtle.Screen()

# method to draw ellipse
def draw(rad):
    # rad --> radius for arc
    for i in range(1):
        turtle.circle(rad, 90)
        turtle.circle(rad // 2, 90)

# Main screen size
screen.setup(500, 500)

# Set screen color
screen.bgcolor('black')

# some integers
val = 10

# turtle speed
turtle.speed(100)
turtle.color("white")
# loop for multiple ellipse
for i in range(36*8):
    # oriented the ellipse at angle = -val
    turtle.seth(-val)

    # drawing shape method
    draw(i)

    # orientation change
    val += 100

# for hiding the turtle
turtle.hideturtle()
turtle.exitonclick()
