bugs=input("do you like bugs?")




def spider():
    import turtle as trtl

    body= trtl.Turtle()

    body.pensize(40)
    body.circle(20)
    leg_amount = 8
    leg_lenght= 70
    leg_angle = 360 / leg_amount
    body.pensize(5)
    n = 0

    while (n < leg_amount/2):
        body.goto(0,20)
        body.setheading(leg_angle-30 *n)
        body.forward(leg_lenght)
        n = n + 1

    import turtle as trtl
    body= trtl.Turtle() 

    leg_amount = 8
    leg_lenght= 70
    leg_angle = 360 / leg_amount
    body.pensize(5)
    n = 0

    while (n < leg_amount/2):
        body.goto(0,20)
        body.setheading(leg_angle+30*n)
        body.forward(leg_lenght)
    n = n + 1


spider()