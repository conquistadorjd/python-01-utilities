from PIL import Image, ImageDraw, ImageFont
import textwrap

image = Image.open('image_crop_input.jpg')
width, height = image.size

print(width)
print(height)

image2 = image.crop((0, 0, height/2, width/2))

width, height = image2.size
print(width)
print(height)

image2.save('image_crop_output.jpg') 