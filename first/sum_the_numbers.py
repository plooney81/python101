# create a list of numbers, and then print their sum

# prompt the user to input a number to go until
# i.e. if the user inputs 5, then the list will be 1 to 5
print('\nInput a number you would like to sum (3 would return the sum of 1 + 2 + 3)')

# while loop that goes until the user inputs an integer correctly
while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('Invalid input, please enter an integer')

# create our list of numbers
list_of_numbers = range(user_input + 1)

# initiate our sum variable which houses the addition of our numbers in the list
sum_var = 0

# for loop that iterates of the numbers in the list and adds that to our variable
for number in list_of_numbers:
    sum_var += number

# print the sum
print(f'The sum from 0 to {user_input} is {sum_var}')