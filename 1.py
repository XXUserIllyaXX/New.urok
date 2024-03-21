from turtle import*
t = Turtle()
t.color("green")
t.shape("circle")
t.speed(0)
t.up()
speed_y = 5
while True:
    t.goto(t.xcor(), t.ycor() - speed_y)
mainloop()