################################################################################################
# fetch quote from Litrating API
# decide fontsize based on quote length
# decide font type based on genre
# decide image based on genre
# write image to image folder
# update wordpress API with quoteimage meta
# post to instagram
# post to twitter
#################################################################################################

from PIL import Image, ImageDraw, ImageFont
import textwrap


fontpath = '/home/conquistador/code/github/python-01-utilities/image/fonts/'
imagepath = '/home/conquistador/code/github/python-01-utilities/image/images/'
img_fraction = 0.50
fontsize =40

image = Image.open('Template Quote V 2.0.jpg')
image_width, image_height = image.size

draw = ImageDraw.Draw(image)

text = "Sample"

print('fontsize',fontsize)
font = ImageFont.truetype(fontpath + 'Unkempt-Regular.ttf', fontsize)
print('font.getsize(text) : ',font.getsize(text))

print(len(text))
while font.getsize(text)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize = fontsize + 1
    font = ImageFont.truetype( fontpath + 'Unkempt-Regular.ttf', fontsize)


print("final font size: ", fontsize)


# textwidth, textheight = draw.textsize(text, font)
 

draw.text((0.25*image_width, 0.25*image_height), text, font=font)
 
image.save('image_add_text_adjustfontsize_output2.png')
 