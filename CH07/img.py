from PIL import Image
import os

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        image_file = Image.open(file)  # open colour image
        image_file = image_file.convert('L')  # convert image to black and white
        image_file.save(file[:-4] + '_grey.png')