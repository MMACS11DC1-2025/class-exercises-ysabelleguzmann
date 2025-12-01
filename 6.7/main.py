#project 67
#ysabelle guzman
#nov 26 25

#START OFF WITH A FUNCTION THAT GOES THROUGH EACH PIXEL PER PICTURE AND DEFINING ITS COLOUR
#TRUE IF FOLLOWS ALONG WITH THE REQUIREMENTS,
#ELSE = FALSE

import time

from PIL import Image

t0 = time.time()

def colour(r, g, b):
    # r <= 235 g <= 48 b <= 89
    if r <= 235 and g <= 48 and b <= 89:
        return "day"
    # r <= 230 g <= 50 b <= 10
    elif r <= 230 and g <= 50 and b <= 10:
        return "night"
    
file = Image.open("6.7/day1.jpg")
t1 = time.time()

file = Image.open("6.7/day2.jpg")

file = Image.open("6.7/day3.jpg")

file = Image.open("6.7/day4.jpg")


width = file.width
height = file.height


for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "day":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x, y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "night":
            red_pixels.append(jb_image[x,y])
           orange_pixels.append(jb_image[x,y])

#images will loop into the function
    file = file.open("6.7/")
