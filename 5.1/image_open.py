from PIL import Image


def colours(r, g, b):
    if 0 >= r <= 255 and 0 >= g <= 255 and 0 >= b <= 255:
        return True
    else:
        return False

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

print(image_green[0,0])

pixel = image_green[0,0]
r = pixel[0]
g = image_green[0,0][1]
b = image_green[0,0][2]

print(colours(r, g, b))

