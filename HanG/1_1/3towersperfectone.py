import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -50
y = -150

# height of tower and a counter for each floor
num_floors = 21
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  rem = floor % 6
  if (rem > 2):  
    painter.color("blue")

  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

x=50
y=-150


num_floors = 21
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("grey")
  rem = floor % 6
  if (rem > 2):  
    painter.color("blue")

  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)



x=0
y=-150

num_floors = 21
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("blue")
  rem = floor % 6
  if (rem > 2):  
    painter.color("grey")

  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()