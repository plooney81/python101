# given a string from the user, print the same string in reverse

# prompt the user for a string
print('\nPlease input a string')

# while loop to make sure the user inputs a string...basically the opposite of the integer version
# so if converting the input to an integer doesn't throw a ValueError(i.e. they just type in a number), 
# then the code will continue to loop until the user gives an string of some type.
while True:
    try:
        # save the user input to a varaible named user_input
        user_input = input('> ')
        to_int = int(user_input)
        print('\nInvalid input, please type a string')
    except ValueError:
        break

# empty variable for the reversed version of the user_input
reverse_input = ''

# loop through each character in the string
for char in user_input:
    # for each character in user input, it adds to the front of our reverse_input variable instead of:
    # reverse_input += char --> which adds to the end...which is what we normally do
    reverse_input = char + reverse_input

# print out the reverse version
print(f'\nThe original string was:\n{user_input}\n\nThe reverse of this is: \n{reverse_input}\n')

# we can also accomplish this by doing
# print(user_input[::-1]) #which is much faster, but yolo