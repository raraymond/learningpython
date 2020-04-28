from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('cropped.png', 'png')


# img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# # filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.convert('L')
# filtered_img.save("grey.png", "png")
# crooked = filtered_img.rotate(90)
# crooked.save('crooked.png', 'png')
# box =
# resized = filtered_img.resize((300, 300))
# resized.save('resized.png', 'png')
# filtered_img.show()
# print(img)
# print(img.format)
# print(img.size)
# print(img.RGB)
# print(dir(img))
