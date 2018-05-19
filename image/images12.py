from PIL import Image, ImageDraw, ImageFont
 
image = Image.open('first.png')
width, height = image.size
 
draw = ImageDraw.Draw(image)
text = "My favorite toy growing up was Polly Pocket. But one gift that I wanted though never received for Christmas was a pair of trampoline moon shoes. You strap them to your feet and they have springs on them, and you can just jump around!"
 
font = ImageFont.truetype('Roboto-Bold.ttf', 12)
textwidth, textheight = draw.textsize(text, font)
 
# calculate the x,y coordinates of the text
margin = 5
x = width - textwidth - margin
y = height - textheight - margin
 
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
 
image.save('cats.png')