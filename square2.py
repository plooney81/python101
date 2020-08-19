# create a NxN square of * characters where N is given from the user input
counter = 0

# prompt the user to enter a var for the square height/width
print('\nPlease enter a number for the height/width of the square')

# while loop that makes sure the user inputted a number, more specifically an integer
while True:
    try:
        # create a var for square width_height and initialize with the user input
        square_width_height = int(input('> '))
        break
    except ValueError:
        print('\nInvalid input, please try inputting a integer')

# creates the square with the user specified params
while counter < square_width_height:
    print('*' * square_width_height)
    counter += 1