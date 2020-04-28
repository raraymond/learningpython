import sys
import os
from PIL import Image

# grab the frist and second argument folder of image/where new images should go
image_folder = sys.argv[1]
# check if new exists, if not create it
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    # print('image processed')
print(image_folder, output_folder)
# loop through proided folder
# covert all images to PNG
# save them to new folder.
