#project 67
#ysabelle guzman
#nov 26 25

#START OFF WITH A FUNCTION THAT GOES THROUGH EACH PIXEL PER PICTURE AND DEFINING ITS COLOUR
#TRUE IF FOLLOWS ALONG WITH THE REQUIREMENTS,
#ELSE = FALSE

import time

from PIL import Image

t0 = time.time()

#defines the colour that represents day (blue), and that represents night (black)
def colour(r, g, b):
    # r <= 235 g <= 48 b <= 89
    if r <= 235 and g <= 48 and b <= 89:
        return "day"
    # r <= 230 g <= 50 b <= 10
    elif r <= 230 and g <= 50 and b <= 10:
        return "night"
    
#list of day/night images 
world = ["6.7/day1.jpg", "6.7/day2.jpg", "6.7/day3.jpg", "6.7/day4.jpg", "6.7/day5.jpg", "6.7/night1.jpg", "6.7/night2.jpg", "6.7/night3.jpg", "6.7/night4.jpg", "6.7/night5.jpg"]

#loops through each image
for image in world:
    file = Image.open(world)
    dn_image = file.load()

#identifies what its pixels for day or night
for i in range(len(world)):
    width = file.width
    height = file.height

    day_pixels = []
    night_pixels = []

    for x in range(width):
        for y in range(height):
            pixel_r = dn_image[x,y][0]
            pixel_g = dn_image[x,y][1]
            pixel_b = dn_image[x,y][2]

            if colour(pixel_r, pixel_g, pixel_b) == "day":
                day_pixels.append(dn_image[x,y])
            if colour(pixel_r, pixel_g, pixel_b) == "night":
                night_pixels.append(dn_image[x,y])

num_day = len(day_pixels)
num_night = len(night_pixels)

total_pixels = width*height

# count how many images there are that assign with the options : day or night, should result with 5 days, 5 nights


# UNIT 6: SORTING SECTION
# in this section, it will sort from the brightest to darkest image.