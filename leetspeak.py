# given a user input convert the string into leetspeak
# what is leetspeak ?
        # A -> 4
        # E -> 3
        # G -> 6
        # I -> 1
        # O -> 0
        # S -> 5
        # T -> 7

# prompt the user to input a string
print('Please input a paragraph')

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
        user_input = user_input
        break

# we need to initiate a dummy variable for saving the new leetspeak paragraph
leetspeak = ''

# initiate a append_character variable, this will hold the character we want to append to our leetspeak
# variable depending on if its a special character (it will be changed to a number), and if its not then
# we append the normal character not changed.
append_character = ''

# for loop to iterate through the userinput string to change the special characters from above
for character in user_input:
    if character.upper() == "A":
        append_character = '4'
    elif character.upper() == "E":
        append_character = '3'
    elif character.upper() == "G":
        append_character = '6'
    elif character.upper() == "I":
        append_character = '1'
    elif character.upper() == "O":
        append_character = '0'
    elif character.upper() == "S":
        append_character = '5'
    elif character.upper() == "T":
        append_character = '7'
    # if the character is not one of these special characters, then we don't need to change that particular character,
    # so we assign append_character to the original value.
    else:
        append_character = character
    
    # we then append the correct character to our leetspeak variable
    leetspeak += append_character

# we then print out the final translation
print(leetspeak)