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
import os
import random

fontpath = '/home/conquistador/code/github/python-01-utilities/image/fonts/'
imagepath = '/home/conquistador/code/images/Litrating.com/files/selected/'

img_fraction = 0.80
fontsize =1

def get_ramdom_image():
	files = os.listdir(imagepath)
	index = random.randrange(0, len(files))
	return files[index]

# image_name = get_ramdom_image()
image_name = 'black-w0.25-h0.25-Template Quote V 3.0.jpg'
image = Image.open(imagepath + image_name)
quote_color = image_name[0:5]
quote_x = float(image_name[7:11])
quote_y = float(image_name[14:17])

image_width, image_height = image.size
draw = ImageDraw.Draw(image)

print('***************************************************************')
print('image_name	:',image_name)
print('quote_color	:',quote_color)
print('quote_x		:',quote_x)
print('quote_y		:',quote_y)
print('image_width	:',image_width)
print('image_height	:',image_height)
print('***************************************************************')


# text = "Sample Sample Sample Sample Sample Sample Sample Sample Sample Sample Sample Sample"
text = '123456789012345678901234567890'

font = ImageFont.truetype(fontpath + 'Unkempt-Regular.ttf', fontsize)
print('fontsize		:',fontsize)
print('font.getsize(text) 	:',font.getsize(text))
print('font.getsize(text) 	:',font.getsize(text)[0]/len(text))
print('length		 	:',len(text))
print('img_fraction*quote_x*image_width : ',img_fraction*quote_x*image_width)
print('***************************************************************')

if (font.getsize(text)[0] <= img_fraction*quote_x*image_width):
	draw.text((quote_x, quote_y), text, font=font)
	print('inside if')
else: 
	print('inside else')
	lines = textwrap.wrap(text, img_fraction*quote_x*image_width)
	line_height = font.getsize('hg')[1]
	print(lines)
	for line in lines:
	    draw.text((quote_x*image_width, quote_y*image_height), line, font=font)
	    quote_y = quote_y + line_height
	    print('font.getsize(text)[line]',font.getsize(line)[0])



	# while font.getsize(text)[0] < img_fraction*quote_x*image.size[0]:
	#     # iterate until the text size is just larger than the criteria
	#     fontsize = fontsize + 1
	#     font = ImageFont.truetype( fontpath + 'Unkempt-Regular.ttf', fontsize)


# print("final font size: ", fontsize)


# # textwidth, textheight = draw.textsize(text, font)

 
image.save('image_main_output.png')
