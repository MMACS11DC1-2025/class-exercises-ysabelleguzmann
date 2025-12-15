#project 67
#ysabelle guzman
#nov 26 25


#START OFF WITH A FUNCTION THAT GOES THROUGH EACH PIXEL PER PICTURE AND DEFINING ITS COLOUR
#TRUE IF FOLLOWS ALONG WITH THE REQUIREMENTS,
#ELSE = FALSE

import time

from PIL import Image

#defines the colour that represents day (blue), and that represents night (black)
def colour(r, g, b):
    # day pixels : blueish
    if 10 <= r <= 125 and 70 <= g <= 178 and 140 <= b <= 255:
        return "day"
    # night pixels : dark
    elif r <= 18 and g <= 16 and b <= 20:
        return "night"
    else:
        return None
    
#list of day/night images 
world = ["6.7/day1.jpg", "6.7/day2.jpg", "6.7/day3.jpg", "6.7/day4.jpg", "6.7/day5.jpg", "6.7/night1.jpg", "6.7/night2.jpg", "6.7/night3.jpg", "6.7/night4.jpg", "6.7/night5.jpg"]

#totals for number of images
day_images = 0
night_images = 0

t0 = time.time()

#loops through each image
for image in world:
    file = Image.open(image)
    dn_image = file.load()

    width = file.width
    height = file.height

    # pixel counter
    day_pixels = []
    night_pixels = []

#checks if pixel matches day or night
    for x in range(width):
        for y in range(height):
            r, g, b = dn_image[x,y]

            if colour(r, g, b) == 'day':
                day_pixels.append((x,y))
            elif colour(r, g, b) == 'night':
                night_pixels.append((x,y))

    #decides whether it is DAY or NIGHT 
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