# counting jelly beans
#import image processing libraries
from PIL import Image

#define a function colour(r,g,b) to return the colour of a pixel
def colour(r, g, b):
    #yellow
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    else:
        return "other"

    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

# create a list to store the pixels that are yellow
yellow_pixels = []

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
            file.putpixel(yellow_pixels, 255, 255, 255)

#gets the length of yellow pixels
num_yellow = len(yellow_pixels)
#total number of pixels in the image
total_pixels = width*height

#calculates the ratio by dividing num_yellow and total_pixels
yellow_ratio = num_yellow / total_pixels

yellow_percent = yellow_ratio * 100
report = "there are {:.2f}% yellow jelly beans".format(yellow_percent)
print(report)
