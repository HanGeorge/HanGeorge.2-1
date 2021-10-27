#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
body= trtl.Turtle()
#this program will make the body of the spider
body.pensize(40)
body.circle(20)
#this part of the program determines the leg lenght, amount and what angle/postion the leg is in.
leg_amount = 8
leg_lenght= 70
leg_angle = 360 / leg_amount
body.pensize(5)
n = 0
#this part of the code actually draws the legs using the comands above.
while (n < leg_amount):
  body.goto(0,20)
  body.setheading(leg_angle *n)
  body.forward(leg_lenght)
  n = n + 1
body.hideturtle()
wn = trtl.Screen()
wn.mainloop()