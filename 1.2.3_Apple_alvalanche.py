import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

letters = ["A", "S", "D", "F", "H" , "H", "J","K", "L"]


apple_list = []
apple_letters = []

for i in range (5):
  apple_list.append(trtl.Turtle())
  apple_letters.append(rand.choice(letters))



def draw_apple(index):
  apple_list[index].penup()
  apple_list[index].shape(apple_image)
  wn.tracer(False)
  apple_list[index].setx(rand.randint(-150,150))
  apple_list[index].sety(rand.randint(-15,100))
  apple_list[index].sety(apple_list[index].ycor()-30)
  apple_list[index].color("white")
  apple_list[index].write(apple_letters[index], align = "center", font=("Arial", 30, "bold")) 
  apple_list[index].sety(apple_list[index].ycor()+30)
  apple_list[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  drop_apple()
  wn.tracer(False)


######################################
letters = ["A", "S", "D", "F", "H" , "H", "J","K", "L"]


apple_list = []
apple_letters = []


def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()
  #draw_apple(index)

def typedA():
  for i in range (5):
   if apple_letters[i] == "A":
    drop_apple(i)

def typedS():
  for i in range (5):
   if apple_letters[i] == "S":
    drop_apple(i)

def typedD():
  for i in range (5):
   if apple_letters[i] == "D":
    drop_apple(i)

def typedF():
  for i in range (5):
   if apple_letters[i] == "F":
    drop_apple(i)

def typedG():
  for i in range (5):
   if apple_letters[i] == "G":
    drop_apple(i)


def typedH():
  for i in range (5):
   if apple_letters[i] == "H":
    drop_apple(i)

def typedJ():
  for i in range (5):
   if apple_letters[i] == "J":
    drop_apple(i)
    
def typedK():
  for i in range (5):
   if apple_letters[i] == "K":
    drop_apple(i)

def typedL():
  for i in range (5):
   if apple_letters[i] == "L":
    drop_apple(i)


#-----function calls-----
for i in range (5):
  draw_apple(i)

wn.onkeypress(typedA, "a")
wn.onkeypress(typedS, "s")
wn.onkeypress(typedD, "d")
wn.onkeypress(typedF, "f")
wn.onkeypress(typedG, "g")
wn.onkeypress(typedH, "h")
wn.onkeypress(typedJ, "j")
wn.onkeypress(typedK, "k")
wn.onkeypress(typedL, "l")

wn.listen()

wn.mainloop()