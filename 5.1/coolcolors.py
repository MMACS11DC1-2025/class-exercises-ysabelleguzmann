def is_green(r, g, b):
    if r <= 24 and g <= 255 and b <= 24:
        return("green")
    if r <= 24 and g <= 24 and b <= 255:
        return("blue")
    if r <= 255 and g <= 24 and b <= 24:
        return("red")
    if 230 < r <= 255 and 230 < g <= 255 and 230 < b <= 255:
        return("white")
    if 25 > r <= 255 and 25 > g <= 255 and 25 > b <= 255:
        return("black")
    if 230 < r <= 255 and 230 < g <= 255 and 25 > b >= 0:
        return("yellow")
    if 230 < r <= 255 and 25 > g >= 0 and 230 < b <= 255:
        return("magenta")