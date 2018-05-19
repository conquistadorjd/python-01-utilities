	
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines

def draw_text(text):    
    # open the background file
    img = Image.open('mountain-road-1556177_1920.jpg')
    
    # size() returns a tuple of (width, height) 
    image_size = img.size
    draw = ImageDraw.Draw(img)
     
    # create the ImageFont instance
    # font_file_path = 'fonts/Avenir-Medium.ttf'
    font = ImageFont.truetype('Roboto-Bold.ttf', size=60)
    # font = ImageFont.truetype(font_file_path, size=50, encoding="unic")
 
    # get shorter lines
    # lines = text_wrap(text, font, image_size[0])
    # print(lines) # ['This could be a single line text ', 'but its too long to fit in one. ']
    lines = text_wrap(text, font, image_size[0])
    line_height = font.getsize('hg')[1]

    x = 10
    y = 20
    for line in lines:
	    draw.text((x, y), line, fill=color, font=font)
	    y = y + line_height
	# img.save('word2.png', optimize=True)

if __name__ == "__main__":
    draw_text("My favorite toy growing up was Polly Pocket. But one gift that I wanted though never received for Christmas was a pair of trampoline moon shoes. You strap them to your feet and they have springs on them, and you can just jump around!")    