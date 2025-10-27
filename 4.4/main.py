import turtle

def draw_tree(level):
    if level == 0:
        turtle.stamp()

    else:
        turtle.forward(30)

        turtle.left(40)
        draw_tree(level-1)

        turtle.right(80)
        draw_tree(level-1)

        turtle.left(40)
        turtle.back(30)


turtle.speed(0)
turtle.left(90)

draw_tree(5)