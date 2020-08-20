# print a triangle with x height, each level adds 2 more * from the last level

# add a counter variable
counter = 0

# ask the user the height they would like the triangle to be
print('\nHow tall would you like your triangle to be:')

# While loop to make sure they inputted the correct data type (i.e. an integer, we can't have 3.5 height of an *, and we cant have "Pete" height either...although that would be cool)
while True:
    try:
        triangle_height = int(input('> '))
        break
    except ValueError:
        print('\nInvalid input, please type an Integer')

# find out how wide our bottom row will be, so we can center the other rows in the following while loop
bottom_width = int((2 * triangle_height)- 1)


# initiate our number of emoji's per level with 1
numb = 1

# side space var is initiated to bottom width - 1
side_spaces = bottom_width - 1

# while loop to print our triangle
while counter < triangle_height:
    # print out the lines worth of left spaces (so we can center the line to our bottom line) and the number of emoji's
    print(' ' * side_spaces + '🥴' * numb)
    numb += 2
    counter += 1
    side_spaces -= 2