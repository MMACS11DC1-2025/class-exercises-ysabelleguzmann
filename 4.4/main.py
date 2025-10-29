import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(40)
    drawTree(level-1, branchLength/1.61)
    
    turtle.right(40)
    drawTree(level-1, branchLength/1.61)
    
    turtle.right(40)
    drawTree(level-1, branchLength/1.61)
    
    turtle.left(40)
    turtle.back(branchLength)
  else:
    turtle.color("green")
    turtle.stamp()
    turtle.color("brown")

def drawSpiral(spins, spiralLength):
  if spins > 0:
    turtle.forward(spiralLength)
    turtle.right(20)
    drawSpiral(spins-1, spiralLength/1.00)
    
    
choice = input('which one would you like to draw? tree or spiral')
levels = input("How many levels do you want me to draw? ")
    
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

if choice == 'tree':
  drawTree(50, 100)
  
elif choice == 'spiral':
  drawSpiral(100, 0)

else:
  print('pls pick one of the choices')

turtle.color("black")
turtle.width(3)
turtle.shape("triangle")
