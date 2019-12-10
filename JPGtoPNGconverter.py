import sys
import os
from PIL import Image
# grab first and second argument
in_folder = sys.argv[1]
out_folder = sys.argv[2]
# check if new/ exists, if not create
if not (os.path.exists(out_folder)):
    os.makedirs(out_folder)
for img_name in os.listdir(in_folder):
     img = Image.open(f'{in_folder}{img_name}')
     split_img_name = os.path.splitext(img_name)[0]
     img.save(f'{out_folder}{split_img_name}.png','png')
     print("All Done!")

