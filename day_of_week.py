# initiate a day of the week variable with an empty string
day_of_the_week = ''

# prompt the user for the day of the week
print('Please enter a of the week between 0 and 6...0 being for Sunday and 6 being for Saturday')

# a while loop that continues to ask the user for an input until a value between 0 and 6 is inputted
while day_of_the_week == '':
    # save the input to a variable called user_input
    user_input = int(input('> '))

    # if elif statement to check what the user inputted and convert to the right day of the week.
    if user_input == 0:
        day_of_the_week = "Sunday"
    elif user_input == 1:
        day_of_the_week = "Monday"
    elif user_input == 2:
        day_of_the_week = "Tuesday"
    elif user_input == 3:
        day_of_the_week = "Wednesday"
    elif user_input == 4:
        day_of_the_week = "Thursday"
    elif user_input == 5:
        day_of_the_week = "Friday"
    elif user_input == 6:
        day_of_the_week = "Saturday"
    else:
        print("Invalid input, please try again.")

print(f'The day of the week corresponding to your input is --> {day_of_the_week}')