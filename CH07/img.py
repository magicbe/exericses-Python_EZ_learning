from PIL import Image
image_file = Image.open("convert_image.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('result.png')