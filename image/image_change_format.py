from PIL import Image, ImageDraw, ImageFont

# jpg to png
image = Image.open('image_change_format_input.jpg')
image.save('image_change_format_output_jpg.png') 

# png to jpg
image = Image.open('image_change_format_output_jpg.png')
image.save('image_change_format_output_jpg_jpg.jpg') 