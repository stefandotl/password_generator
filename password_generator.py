import PIL
import random

"""This module creates an DsiN-password-card"""

alphabet_small = "abcdefghijklmnopqrstuvwxyz"
alphabet_large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = "0123456789"
first_column = [1,2,3,4,5,6,7,8,9,10,11,12]
top_col = iter(first_column)
special_signs = "!&@$#"

all_signs = alphabet_small + alphabet_large + numbers + special_signs

line_arr = []
all_array = []

with open("textfile.txt", "w") as txt_file:

    for row in range(13):
        if row == 0:  # prints the first line
            print(" " + alphabet_large, file=txt_file, end="")
            all_array.append(alphabet_list)
        else:
            for column in range(27):

                if column == 0:
                    first_char = next(top_col)
                    print(first_char, file=txt_file, end="")
                    line_arr.append(first_char)
                else:
                    rand_num = random.randint(0, 66)
                    print(all_signs[rand_num], file=txt_file, end="")
                    line_arr.append(all_signs[rand_num])
        
            all_array.append(line_arr)
            line_arr = []
        print("\n", file=txt_file)

print(all_array)