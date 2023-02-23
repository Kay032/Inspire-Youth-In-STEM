# set the number of rows in the diamond
num_rows = 9

# iterate over the rows
for i in range(num_rows):
    # calculate the number of spaces and stars in this row
    num_spaces = abs(num_rows // 2 - i)
    num_stars = num_rows - 2 * num_spaces
    
    # print the spaces and stars in this row
    print(' ' * num_spaces + '*' * num_stars)



