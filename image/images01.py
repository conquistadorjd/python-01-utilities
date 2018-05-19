import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans.ttf",25)
img=Image.new("RGBA", (200,200),(120,20,20))
draw = ImageDraw.Draw(img)
# draw.text((0, 0),"This is a test",(255,255,0),font=font)
draw.text((0, 0),"This is a test",(255,255,0))
draw.chord((100, 75, 125, 100), 0, 360, fill='green')
draw.chord((75, 100, 100, 125), 0, 360, fill='blue')
draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')
draw = ImageDraw.Draw(img)

img.save("test.png")