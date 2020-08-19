# Function that checks to see if the input is an integer, if it isn't an integer, then the while
# loop will not 
def is_it_a_integer():
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('\nInvalid input, please try again')


# prompt the user for the width and the height of the box
print('\nInput the width of your box')
user_width = is_it_a_integer()


# prompt the user for the height of the box
print('\nInput the height of your box')
user_height = is_it_a_integer()

# create our box based off the user inputs
# first create the top of the box
print('*' * user_width)

# while loop for the sides of the box
i = 0
while i < (user_height - 2):
    print('*' + ' ' * (user_width - 2) + '*')
    i = i + 1


# then create the bottom of the box
print('*' * user_width)