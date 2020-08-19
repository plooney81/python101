# Initiate our change_to_fahrenheit variable to -9999
change_to_fahrenheit = 0

# Prompt the user to enter a degrees in Celsius
print('Enter degrees in Celsius and see what happens:')

# While loop that continues to ask for user input if it doesn't
while change_to_fahrenheit == 0:

    # capture the user input to a variable
    user_input = input('> ')

    # if the user correctly inputs a number
    if user_input.isnumeric():
        # take user input and convert to fahreheneit 
        user_input = float(user_input)
        change_to_fahrenheit = ((user_input * (9/5)) + 32)
    else:
        print('Invalid input try again')

# print the new degrees
print(f'Your degrees in fahrenheit are: {change_to_fahrenheit}')