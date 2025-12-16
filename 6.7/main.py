#project 67
#ysabelle guzman
#nov 26 25


#START OFF WITH A FUNCTION THAT GOES THROUGH EACH PIXEL PER PICTURE AND DEFINING ITS COLOUR
#TRUE IF FOLLOWS ALONG WITH THE REQUIREMENTS,
#ELSE = FALSE

import time

from PIL import Image

#defines the colour that represents day, and that represents night
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

percentage = []
#loops through each image
for i in range(len(world)):
    pictures = world[i]
    file = Image.open(pictures)
    dn_image = file.load()

    width = file.width
    height = file.height

    # pixel counter
    day_pixels = []
    night_pixels = []

#checks if pixel matches day or night
    for x in range(width):
        for y in range(height):
            pixels = dn_image[x, y]
            pixel_r = pixels[0]
            pixel_g = pixels[1]
            pixel_b = pixels[2]
            colour_type = colour(pixel_r, pixel_g, pixel_b)

            if colour_type == 'day':
                day_pixels.append((x,y))
            elif colour_type == 'night':
                night_pixels.append((x,y))

    #decides whether it is DAY or NIGHT
    if day_pixels > night_pixels:
        day_images += 1
        print("Classified as a DAY IMAGE")
    else:
        night_images += 1
        print("Classified as a NIGHT IMAGE")

num_day = len(day_pixels)
num_night = len(night_pixels)
total_pixels = width * height

t1 = time.time()
total_time = t1 - t0

timing = "it took {:.2f}s to run this".format(total_time)
print(timing)

#total_day = n
#total_night = num_night

if total_day > 0:
    day_percentage = total_night / * 100

output = "Images {}, it is {:.2f}% day.".format(world[i], day_percentage)
print(output)

# UNIT 6: SORTING SECTION
# in this section, it will sort from the brightest to darkest image.

for i in range(i + 1, len(percentage)):
    largest_index = i

    for j in range(i + j, len(percentage)):
        if percentage[j][0] > percentage[largest_index][0]:
            largest_index = j

    percentage[i], percentage[largest_index] = percentage[largest_index], percentage[i]

    print("\n Top 5 most burnt breads are: ")
    for i in percentage[:5]:
        print(str(i[1]) + " with " + f"{i[0]:.2f}% " + " burn. ")

def search(list_of_lists, query):
    querymin = query - 5
    search_start_index = 0
    search_end_index = len(list_of_lists) - 1

    while search_start_index <= search_end_index:
        midpoint = int((search_start_index + search_end_index) / 2)

        if list_of_lists[midpoint][0] <= query and list_of_lists[midpoint][0] >= querymin:
            return list_of_lists[midpoint][1]
        
        elif list_of_lists[midpoint][0] > query and list_of_lists[midpoint][0] >= querymin:
            search_start_index = midpoint + 1

        else:
            searchend_index = midpoint - 1

search_target = 100.00
found_target = search(percentage, search_target)

if found_target:
    print("\nFound bread with approximately {:.2f}% burn: {}".format(search_target, found_target))
else:
    print("\nNo bread found with approximately {:.2f}% burn".format(search_target))


    