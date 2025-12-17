#exercise 8
#outputs a statement about the image
import time
t0 = time.time()

from PIL import Image

def colour(r, g, b):
    if 220 > r > 100 and 40 > g > 23 and 255 > b > 115 :
        return "blue"
    else:
        return "other"
    
file = Image.open("5.1/mountains.jpg")
mtn_image = file.load()

blue_pixels = []

width = file.width
height = file.height


for x in range(width):
    for y in range(height):
        pixel_r = mtn_image[x,y][0]
        pixel_g = mtn_image[x,y][1]
        pixel_b = mtn_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "blue":
            blue_pixels.append(mtn_image[x,y])
            print("it's mostly blue")

t3 = time.time()

num_b = len(blue_pixels)

total = width*height
file.save("output.png", "png")

b_ratio = num_b / total
num_b = len(blue_pixels)
b_percent = b_ratio * 100

report = "there is {:.2f}% blue jelly beans.".format(b_percent)
print(report)

entire = t3 - t0

time = "it took {:.3f}s to do the entire code".format(entire)
print(time)

        