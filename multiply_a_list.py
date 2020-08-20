# create a list of numbers, using a val specified by the user multiply each number in the list by that value and then print a new list just with the multiplied values

import random

def is_it_an_integer():
    # while loop that goes until the user inputs an integer correctly
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('Invalid input, please enter an integer')

# prompt the user to get our upper bounds for a random num
# i.e. if the user inputs 5, then we could get a random number from 0 to 5
print('\nInput a number you want for the upper bounds of a random int')
user_input = is_it_an_integer()

# prompt the user to get how long they would like the list to be
print('\nInput a number you want for the length of our list')
list_length = is_it_an_integer()

# prompt the user to get the multiplication factor
print('\nInput a number you want to multiply the list by')
multiplication_factor = is_it_an_integer()

# create our empty list
list_of_numbers = []

# for loop for our list
for index in range(0, list_length):
    # create a new random number
    # random.randint(a,b) returns a random integer that is between a and b
    random_number = random.randint(0, user_input)

    # append our random number
    list_of_numbers.append(random_number)

# create an empty array for our multiplied numbers
multiplied_numbers = []

# now we loop through and find out which one of the number are positive
for numbers in list_of_numbers:
    # multiply numbers by our multiplication factor and save to a new variable name mult
    mult = numbers * multiplication_factor
    # append mult to our list named multiplied_numbers
    multiplied_numbers.append(mult)

# print the old list and then print our new list
print(f'\nOur original list is: \n{list_of_numbers}')
print(f'\nHere is the list multiplied by {multiplication_factor}: \n{multiplied_numbers}\n')