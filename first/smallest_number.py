# create a list of numbers, print the smallest number

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

# create our empty list
list_of_numbers = []

# for loop for our list
for index in range(0, list_length):
    # create a new random number
    # random.randint(a,b) returns a random integer that is between a and b
    random_number = random.randint(0, user_input)

    # append our random number
    list_of_numbers.append(random_number)

# initiate a variable that keeps track of the lowest number so far
# we initiate it to the bounds that the user gave + 1 becuase we know that whatever number that is in the list 
# should be lower than that
smallest_number = user_input + 1

# now we loop through and find out which one of the numbers is smallest
for numbers in list_of_numbers:
    # if the current number in the list is higher than hgihest_numb, then we assign that number to highest number
    if numbers < smallest_number:
        smallest_number = numbers

# print the variable highest_numb
print(f'Our list is:')
print(list_of_numbers)
print(f'The lowest number in the list is: {smallest_number}')