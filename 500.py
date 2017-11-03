import turtle
turtle.colormode(255)#bring in colormode
bob=turtle.Turtle()
rob=turtle.Turtle()
bob.width(5)
rob.width(0.1)
bob.speed(1000)
rob.speed(1000)
turtle.bgcolor('black')
#c=(r,g,b)

c=(0,145,0)#c is a variable to store the value
for times in range(100):
 
    for c in ["red","cyan","black"]:
        bob.color(c)
        bob.circle(1)
        bob.forward(times*6)
        bob.right(120)
        bob.left(2)

        rob.penup()
        rob.goto(1, 0)
        rob.pendown()
    
        rob.right(2)
        
        rob.color("white")#red
        rob.forward(100)
        rob.right(30)
        rob.forward(20)
        rob.left(60)
        rob.forward(50)
        rob.right(30)

        
        
    

turtle.done()

