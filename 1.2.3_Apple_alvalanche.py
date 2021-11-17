#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
def new_spot():
    apple.showturtle()
    new_xpos=rand.randint(-100,100)
    new_ypos=rand.randint(-100, 100) 
    
    apple.goto(new_xpos,new_ypos)

#apple.right (90)
#apple.forward(200)

def roll():
    apple_xcor=rand. randint(-200,200)
    apple_ycor=-200
    apple.goto(apple_xcor, apple_ycor)
    apple.hideturtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  apple.penup()
  active_apple.shape(apple_image)
  roll()
  new_spot()
  
  wn.update()

def drop_fruit(): 
    draw_apple()

wn.onkeypress(drop_fruit, "a")
draw_apple(apple)

#-----function calls-----
drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
wn.onkeypress(draw_an_A, "a")
draw_apple(apple)
wn.listen()

wn.mainloop()

#-----function calls-----



# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.

