# Prompt the user to enter a degrees in Celsius
print('Enter degrees in Celsius and see what happens:')

# While loop that continues to ask for user input if the user inputs anything other than a number.
while True:

    # try to run the following block, if there is a type error (i.e. the user entered a string), then the except clause will execute.
    try:
        # assigns the input to a variable named user input
        user_input = float(input('> '))
        # take user input and convert to fahreheneit 
        change_to_fahrenheit = ((user_input * (9/5)) + 32)
        # need to break out of our while loop if the user inputted a number and 
        # we did not get a ValueError
        break
    except ValueError:
        print('Invalid input try again')

# print the new degrees
print(f'You inputted {user_input} degrees Celsius, which is {change_to_fahrenheit} degrees Fahrenheit')