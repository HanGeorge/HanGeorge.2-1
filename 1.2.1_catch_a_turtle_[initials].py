# a121_catch_a_turtle.py
import turtle as trtl
import random as rand
#-----import statements-----
spot_color = ("pink")
spot_shape= "circle"
spot_size= 2 

#-----game configuration----#

#-----initialize turtle-----
spot=trtl.Turtle()
spot.speed(0)
#-----game functions--------
spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)


def spot_clicked(x, y):
    change_position()

def change_position(): 
    spot.penup()
    spot.hideturtle()
    new_xpos=rand.randint(-200,200)
    new_ypos=rand.randint(-200,200)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()

#-----events----------------
spot.onclick(spot_clicked)
wn=trtl.Screen()
wn.mainloop()