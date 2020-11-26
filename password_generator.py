from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os

import matplotlib.pyplot as plt
import numpy as np
import random

"""This module creates an DsiN-password-card"""
#todo: make default Font!

width = 100
height = 100
rows = 12 + 2
columns = 26 + 2

def make_imgs(char_arr):
    counter = 0     # counts all images
    for i, line in enumerate(char_arr):
        for j, char in enumerate(line):
            counter += 1
            if i == 0 or i == 13 or j==0 or j==27:
                color = "lightgreen"
            else:
                if i%2 == 0:
                    color = "lightgray"
                else:
                    color = "white"
            img = Image.new("RGB", (width, height), color=color)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 80)
            draw.rectangle([0,0,99,99], None, 0, 2)
            draw.text((50, 53), str(char), fill="black", anchor="mm", font=font)
            img_name = "imgs/" + str(counter) + ".jpg"
            img.save(img_name)


alphabet_small = "abcdefghijklmnopqrstuvwxyz"
alphabet_large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_list = list("#ABCDEFGHIJKLMNOPQRSTUVWXYZ#")
numbers = "0123456789"
first_column = [1,2,3,4,5,6,7,8,9,10,11,12]
top_col = iter(first_column)
special_signs = "!&@$#"

all_signs = alphabet_small + alphabet_large + numbers + special_signs

line_arr = []
all_array = []
i_count = 1
j_count = 1

with open("textfile.txt", "w") as txt_file:
    for row in range(rows):
        if row == 0 or row == 13:  # prints the first line
            print(alphabet_list, file=txt_file, end="")
            all_array.append(alphabet_list)
        else:
            for column in range(columns):

                if column == 0:                    
                    print(i_count, file=txt_file, end="")                    
                    line_arr.append(i_count)
                    i_count += 1

                elif column == 27:
                    print(j_count, file=txt_file, end="")                    
                    line_arr.append(j_count)
                    j_count += 1

                else:
                    rand_num = random.randint(0, 66)
                    print(all_signs[rand_num], file=txt_file, end="")
                    line_arr.append(all_signs[rand_num])
        
            all_array.append(line_arr)
            line_arr = []
        print("\n", file=txt_file)

arr_np = list(np.array(all_array))

make_imgs(arr_np)

img_arr = []

num_if_imgs = len(os.listdir('./imgs/'))+1

for i in range(1, num_if_imgs):

    img_dir = 'imgs/' + str(i) + '.jpg'  
    opened_img = Image.open(img_dir)
    img_arr.append(opened_img)

width_sum = 28*width
height_sum = 14*height

whole_image = Image.new("RGB", (width_sum, height_sum))

x_offset = 0
y_offset = 0

for img in img_arr:
    whole_image.paste(img, (x_offset, y_offset))
    x_offset += width
    if x_offset >= width_sum: 
        x_offset = 0  
        y_offset += height

whole_image.save("Safe_Card.jpg")


    