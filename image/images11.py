from PIL import Image
image = Image.open('first.png') 
print(image.size, image.format) 
# print(image.size[0])
# print(type(image.size[0]))
# (350, 250) PNG