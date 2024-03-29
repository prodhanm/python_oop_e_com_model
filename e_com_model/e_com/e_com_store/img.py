import os
from PIL import Image

img_path = "./static/img/Final_Fantasy_7.jpg"
new_size = (400,450)  # Set the desired size for the top of the web page

def new_image(image_path, new_size):
    with open(image_path, 'rb') as f:
        image = Image.open(f)
        resize_image = image.resize(new_size, Image.LANCZOS)
        resize_image.save('./static/img/FF7.png')

new_image(img_path, new_size)



''' def resize_image(img_path, new_size):
    image = Image.open(img_path)
    resize_image = image.resize(new_size)
    resize_image.save('./static/img/hero_2.jpg')
    return resize_image '''