#project 67
#ysabelle guzman
#nov 26 25

import time

from PIL import Image

#list of day/night images 
world = ["6.7/day1.jpg", "6.7/day2.jpg", "6.7/day3.jpg", "6.7/day4.jpg", "6.7/day5.jpg", "6.7/night1.jpg", "6.7/night2.jpg", "6.7/night3.jpg", "6.7/night4.jpg", "6.7/night5.jpg"]
percentage = []

#defines the colour that represents day, and that represents night
def colour(r, g, b):
    #dark blue
    if 0 <= r <= 60 and 60 <= g <= 120 and 110 <= b <= 255:
        return "dark blue"
    #blue
    elif 50 <= r <= 90 and 150 <= g <= 190 and 230 <= b <= 255:
        return "blue"
    # night pixels : dark
    elif 5 <= r <= 10 and 8 <= g <= 16 and 19 <= b <= 24:
        return "night"
    else:
        return None


#loops through each image
for img in world:
    t0 = time.time()

    file = Image.open(img)
    file = file.resize((200, 200)) #Defaults each image into 200x200
    pixels = file.load()

    width = file.width
    height = file.height

    total_pixels = width*height

    # pixel counter
    day_pixels = 0
    night_pixels = 0

#checks if pixel matches day or night
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            result = colour(r, g, b)

            if result == "blue" or result == "dark blue":
                day_pixels += 1
            elif result == "night":
                night_pixels += 1

    day_percent = (day_pixels / total_pixels) * 100
    t1 = time.time()
    total_time = t1 - t0

    percentage.append([day_percent, img, total_time])

    print(f"{img}")
    print(f"    DAY: {day_percent:.2f}%")
    print(f"    TIME: {total_time:.2f} seconds\n")


# UNIT 6: SORTING SECTION
# in this section, it will sort from the brightest to darkest image.

#SELECTION SORT
for i in range(len(percentage)):
    largest_index = i
    for j in range(i + 1, len(percentage)):
        if percentage[j][0] > percentage[largest_index][0]:
            largest_index = j

    percentage[i], percentage[largest_index] = percentage[largest_index], percentage[i]

# print sorted results
print("Images sorted from most day (brightest) to most night (darkest):\n")
for item in percentage:
    print(f"{item[1]} has {item[0]:.2f}% day")

#BINARY SEARCH
def binary_search_day(images, target):

    low = 0
    high = len(images) - 1

    lower = target - 1
    higher = target + 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = images[mid][0]
        
        if lower <= mid_value <= higher:
            return images[mid]
        
        elif mid_value < lower:
            high = mid - 1

        else:
            low = mid + 1

    return None
   

search_target = 33.0

result = binary_search_day(percentage, search_target)


if result:
    print("\nBinary Search Results:")
    print(f"IMAGE: {result[1]}")
    print(f"DAY: {result[0]:.2f}% ")
    print(f"TIME: {result[2]:.2f}s")


else:
    print("\nNo image found near {search_target:.2f}% day")


    