import turtle

turtle = turtle.Turtle()
turtle.penup()

def drawTree(level, branchLength): # draws a tree
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


def drawSpiral(spins): # draws a spiral
  if spins < 10:
    return
  turtle.forward(spins)
  turtle.right(100)
  drawSpiral(spins - 10)
    
    
# asks which one to draw
# asks how many levels to draw
choice = input('which one would you like to draw? tree or spiral')
levels = input("How many levels do you want me to draw? ")
    
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.left(90)

# prints out whichever one the user chooses

if choice == 'tree':
  turtle.pendown()
  drawTree(int(levels), 50)
  turtle.color("brown")
  
  
elif choice == 'spiral':
  
  turtle.pendown()
  drawSpiral(int(levels))

else:
  print('pls pick one of the choices')

turtle.color("black")
turtle.width(3)
turtle.shape("triangle")
turtle.done()
