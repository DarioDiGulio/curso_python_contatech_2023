import turtle

colors = ["blue"]
radius = 30
num_circles = 40
angle = 15
start_angle = 30

cantbord = 24

turtle.speed(0)
turtle.hideturtle()

for i in range(num_circles):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(start_angle)
    turtle.pendown()

    for j in range(cantbord):
        turtle.color(colors[j % len(colors)])
        turtle.forward(radius)
        turtle.right(angle)
    start_angle += 10

turtle.done()
