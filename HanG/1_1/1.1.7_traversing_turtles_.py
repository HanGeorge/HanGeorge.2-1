import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  my_turtles.append(t)
  

trtl.setheading=90
startx = 0
starty = 0
startdir=45

#
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading (startdir)
  t.forward(50)
  t.left(45)
  

  startx = t.xcor()
  starty = t.ycor()
  startdir= t.heading()

wn = trtl.Screen()
wn.mainloop()