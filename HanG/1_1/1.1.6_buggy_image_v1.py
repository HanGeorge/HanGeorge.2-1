#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
body= trtl.Turtle()
body.pensize(40)
body.circle(20)
leg_amount = 8
leg_lenght= 70
z = 1000 / leg_amount
body.pensize(5)
n = 0
while (n < leg_amount):
  body.goto(0,0)
  body.setheading(z*n)
  body.forward(leg_lenght)
  n = n + 1
body.hideturtle()
wn = trtl.Screen()
wn.mainloop()