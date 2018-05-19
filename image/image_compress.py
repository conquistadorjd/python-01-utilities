from PIL import Image, ImageDraw, ImageFont

image = Image.open('image_compress_input.jpg')
image.save('image_compress_output.jpg',quality=50) 