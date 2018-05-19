from PIL import Image, ImageDraw, ImageFont
import textwrap

image = Image.open('image_resize_input.png')
width, height = image.size

print(width)
print(height)

image = image.resize((500, 500), Image.ANTIALIAS)

width, height = image.size

print(width)
print(height)

image.save('image_resize_output.jpg') 