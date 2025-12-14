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
    # day pixels : blueish
    if r >= 235 and g >= 48 and b >= 89:
        return "day"
    # night pixels : dark
    elif r <= 50 and g <= 50 and b <= 10:
        return "night"
    
#list of day/night images 
world = ["6.7/day1.jpg", "6.7/day2.jpg", "6.7/day3.jpg", "6.7/day4.jpg", "6.7/day5.jpg", "6.7/night1.jpg", "6.7/night2.jpg", "6.7/night3.jpg", "6.7/night4.jpg", "6.7/night5.jpg"]

#totals for number of images
day_images = 0
night_images = 0

#loops through each image
for image in world:
    file = Image.open(image)
    dn_image = file.load()


for i in range(len(world)):
    width = file.width
    height = file.height

    # pixel counter
    day_pixels = 0
    night_pixels = 0

#checks if pixel matches day or night
    for x in range(width):
        for y in range(height):
            r, g, b = dn_image[x,y]

            if colour(r, g, b) == 'day':
                day_pixels += 1
            elif colour(r, g, b) == 'night':
                night_pixels += 1

    #decides whether it is DAY oe NIGHT
    if day_pixels > night_pixels:
        day_images += 1
        print("Classified as a DAY IMAGE")
    else:
        night_images += 1
        print("Classified as a NIGHT IMAGE")

print("\n TOTAL RESULTS")
print("Number of DAY Images: ", day_images)
print("Number of NIGHT Images:  ", night_images)

t1 = time.time()
total_time = t1 - t0
timing = "it took {:.2f}s to run this".format(total_time)
print(timing)

# UNIT 6: SORTING SECTION
# in this section, it will sort from the brightest to darkest image.