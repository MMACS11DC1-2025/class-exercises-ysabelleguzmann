import turtle

#sets up the turtle shape, color, speed, size of shape
turtle = turtle.Turtle()
turtle.color("brown")
turtle.width(1)
turtle.shape("triangle")
turtle.speed(0)
turtle.penup()

# the colour choices stored in a dictionary
palette = {"morning": "#FE7E0F", "night": "#191970", "sunrise": "#FFC0CB", "sunset": "#800080"}


def drawTree(level, branchLength, color): # draws a tree
  if level > 0: #draws tree branches if level is over 0
    turtle.forward(branchLength)
    turtle.left(20)
    drawTree(level-1, branchLength/1.50, color)
    
    turtle.right(40)
    drawTree(level-1, branchLength/1.50, color)
    
    turtle.left(20)
    turtle.back(branchLength)
    
    
  else:
    turtle.color(color)
    turtle.stamp()
    turtle.color("brown")


def drawStar(spins, color): # draws a spiral
  if spins < 10: # base case, stops when spins is less than 10
    return
  turtle.color(color)
  turtle.forward(spins)
  turtle.right(200)
  drawStar(spins - 5, color)
    
    
# asks which one to draw
# asks how many levels to draw

choice = input('which one would you like to draw? tree or star')
levels = int(input("How many levels do you want me to draw? "))
vibe = input('what vibe? morning, night, sunset, sunrise?')
    
color = palette[vibe] if vibe in palette else vibe

turtle.goto(40, -210)
turtle.left(90)
turtle.pendown()

# prints out whichever one the user chooses unless user selects not one of choices

if choice == "tree":
    turtle.color("brown")
    drawTree(levels, 100, color)
    
elif choice == "star":
    drawStar(levels, color)
    
else: 
    print("Please pick either 'tree' or 'star'.")

turtle.done()