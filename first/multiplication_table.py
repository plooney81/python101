# print the multiplication table for numbs 1 up to 10

# prompt the user to input a number they would like to multiplication tables for
print('\nPlease enter a number (integer) you would like to see the multiplication tables for')

# while loop for our try except to make sure the user actually inputs an integer
# if they don't enter an integer (i.e. we get a ValueError) than it will continue to ask them for another input
while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('\nInvalid input, try again and input an integer')

# initiate our outer loop counter as 1
outer_number = 1
# we want the outer loop to loop 10 times so we could say <= 10 or < 11
while outer_number <= user_input:

    # we need to reinitiate the inner loop counter for every outer loop sequence so the inner loop sequeuence will actual complete, 
    # if we initiate the inner_number up top (i.e. under the outer_number initiation) then it will only print out the table for the first outer number
    inner_number = 1
    while inner_number <= user_input:
        multiplication = outer_number * inner_number
        print(f'{outer_number} X {inner_number} = {multiplication}')
        inner_number += 1

    # incriment our outer_number variable
    outer_number += 1