from PIL import Image

# open image
img = Image.open(r"C:\Users\20100\Downloads\1280px-Sunflower_from_Silesia2.jpg")  # put your image file name here
pixels = img.load()  # access pixel data

width, height = img.size

# set left quarter to black
for x in range(width // 4):      # only the left quarter
    for y in range(height):
        pixels[x, y] = (0, 0, 0)  # black pixel

# save the modified image
img.save("output.jpg")
print("Image saved as output.jpg")
