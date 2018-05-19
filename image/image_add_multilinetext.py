from PIL import Image, ImageDraw, ImageFont
import textwrap

image = Image.open('Template Quote V 2.0.jpg')
width, height = image.size

image_size = image.size
 
draw = ImageDraw.Draw(image)
text = "My favorite toy growing up was Polly Pocket. But one gift that I wanted though never received for Christmas was a pair of trampoline moon shoes. You strap them to your feet and they have springs on them, and you can just jump around!"
 
font = ImageFont.truetype('Unkempt-Regular.ttf', 40)
textwidth, textheight = draw.textsize(text, font)
 
# calculate the x,y coordinates of the text
margin = 5
# x = width - textwidth - margin
# y = height - textheight - margin
x = 150
y = 150

lines = textwrap.wrap(text, width=40)
line_height = font.getsize('hg')[1] 

# print("lines",lines)
# print("line_height",line_height)
print(width)
print(image_size[0])
# draw watermark in the bottom right corner
# draw.text((x, y), text, font=font)
for line in lines:
    width, height = font.getsize(line)
    draw.text((x, y), line, font=font)
    y = y + line_height
    print(line)

y = y + line_height
draw.text((500, y), "-- author", font=font)
 
image.save('image_add_multilinetext_output.jpg')
 
######################################################################## 
# draw watermark in the bottom right corner
# draw.text((x, y), text, font=font)
# h= height
# w = width
# FOREGROUND = (255, 255, 255)


# lines = textwrap.wrap(text, width=40)
# y_text = h


# for line in lines:
#     width, height = font.getsize(line)
#     draw.text(((w - width) / 2, y_text), line, font=font, fill=FOREGROUND)
#     y_text += height
 
# image.save('cats.png')

# import textwrap
# lines = textwrap.wrap(text, width=40)

# print(text)
# print(lines)

