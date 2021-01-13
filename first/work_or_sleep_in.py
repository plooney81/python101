# initiate a work or sleep in variable with an empty string
work_or_sleep_in = ''

# prompt the user for the day of the week
print('Please enter a of the week between 0 and 6...0 being for Sunday and 6 being for Saturday')

# a while loop that continues to ask the user for an input until a value between 0 and 6 is inputted
while work_or_sleep_in == '':
    # save the input to a variable called user_input
    user_input = int(input('> '))

    # if elif statement to check what the user inputted and convert to the right day of the week.
    if user_input == 0 or user_input == 6:
        work_or_sleep_in = "Sleep in..It's the weekend"
    elif user_input > 0 and user_input < 6:
        work_or_sleep_in = "GO TO WORK"
    else:
        print("Invalid input, please try again.")

print(f'Should you work or sleep in today: {work_or_sleep_in}')