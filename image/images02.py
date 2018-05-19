# import required classes
 
from PIL import Image, ImageDraw, ImageFont
 
# create Image object with the input image
 
image = Image.open('mountain-road-1556177_1920.jpg')
 
# initialise the drawing context with
# the image object as background
 
draw = ImageDraw.Draw(image)


# create font object with the font file and specify
# desired size
 
font = ImageFont.truetype('Roboto-Bold.ttf', size=60)

print(font) 
# starting position of the message
 
(x, y) = (50, 50)
message = "My favorite toy growing up was Polly Pocket. But one gift that I wanted though never received for Christmas was a pair of trampoline moon shoes. You strap them to your feet and they have springs on them, and you can just jump around!"
color = 'rgb(0, 0, 0)' # black color

print(message) 
# draw the message on the background 
draw.text((x, y), message, fill=color, font=font)

(x, y) = (150, 150)
name = '--Lucy Hale'
color = 'rgb(255, 255, 255)' # white color
draw.text((x, y), name, fill=color, font=font)

print(color) 
# save the edited image
 
print(image)
image.save('mountain-road-1556177_1920-New.png')