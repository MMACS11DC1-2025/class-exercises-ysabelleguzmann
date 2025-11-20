# counting jelly beans
#import image processing libraries
from PIL import Image

#define a function colour(r,g,b) to return the colour of a pixel
def colour(r, g, b):
    #yellow
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    elif r > 160 and g > 0 and b > 1:
        return "red"
    elif r > 15 and g > 90 and b > 15:
        return "green"
    elif r > 45 and g > 55 and b > 178:
        return "blue"
    elif r > 210 and g > 110 and b < 10:
        return "orange"
    else:
        return "other"

    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

# create a list to store the pixels that are yellow
yellow_pixels = []
red_pixels = []
green_pixels = []
blue_pixels= []
orange_pixels = []

#go through all the pixels in the image
width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x, y), (255, 255, 255))

        

#gets the length of yellow pixels
num_yellow = len(yellow_pixels)
num_red = len(red_pixels)
num_green = len(green_pixels)
num_blue = len(blue_pixels)
num_orange = len(orange_pixels)


#total number of pixels in the image
total_pixels = width*height
file.save("output.png", "png")

#calculates the ratios of colours and total_pixels
yellow_ratio = num_yellow / total_pixels
red_ratio = num_red / total_pixels
green_ratio = num_green / total_pixels
blue_ratio = num_blue / total_pixels
orange_ratio = num_orange / total_pixels

#determines number of pixels of each colour
num_yellow = len(yellow_pixels)
num_red = len(red_pixels)
num_green = len(green_pixels)
num_blue = len(blue_pixels)
num_orange = len(orange_pixels)

yellow_percent = yellow_ratio * 100
red_percent = red_ratio * 100
green_percent = green_ratio * 100
blue_percent = blue_ratio * 100
orange_percent = orange_ratio * 100

report = "there are {:.2f}% yellow jelly beans, {:.2f}% red jelly beans, {:.2f}% green jelly beans, {:.2f}% green jelly beans".format(yellow_percent)
print(report)
