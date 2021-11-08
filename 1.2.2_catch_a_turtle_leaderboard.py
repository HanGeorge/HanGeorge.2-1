
leaderboard_file_name = "1.2.2_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

# a121_catch_a_turtle.py
import turtle as trtl
import random as rand
import leaderboard as lb
#-----import statements-----
spot_color = ("pink")
spot_shape= "circle"
spot_size= 2 

#-----game configuration----#

#-----initialize turtle-----
spot=trtl.Turtle()
#spot.speed(0)
#-----game functions--------
spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)
score_writer= trtl.Turtle()
score_writer.penup()
score_writer.goto (200,200)
score_writer.hideturtle()

def font_setup():
    ("Arial", 20, "normal")


colors = ["red", "blue", "green"]
size = [1, 2, 1.5,4 ]



def spot_clicked (x,y):
    global timer_up
    if(not timer_up):
        update_score()
        color_change()
        change_size()
        change_position()
    else:
        score_writer.hideturtle()
        update_score()
    
    
def change_position(): 
    #leave_a_mark()
    spot.penup()
    spot.hideturtle()
    new_xpos=rand.randint(-200,200)
    new_ypos=rand.randint(-200,200)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()
    


def leave_a_mark():
    spot.fillcolor(rand.choice(colors[1:]))
    spot.stamp()
    spot.fillcolor(colors[0]) 


score=0
def update_score ():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

wn=trtl.Screen()
#wn.setup(width=1920, height=1080)
wn.bgcolor("light green")

counter =  trtl.Turtle()
counter.penup()
counter.goto(-200,200)
counter.hideturtle()
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
def countdown():
  global timer, timer_up
  counter.clear()
  
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    spot.hideturtle()
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def change_size():
    new_size = rand.choice(size)
    spot.shapesize(new_size)

def color_change():
    new_color = rand.choice(colors)
    spot.color(new_color)


#-----events----------------
spot.onclick(spot_clicked)
wn=trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()