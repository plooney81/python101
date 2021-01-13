# Tip calculator
# Ask for the total bill
# Ask for the tip level --> 3 levels: bad, fair, good

def checks_if_float():
    while True:
        try:
            return float(input('> '))
        except ValueError:
            print('\nInvalid input, please try again with a number')

def tip_level():
    print('Enter the tip level\nType: \'bad\' \'fair\' or \'good\'')
    while True:
        tip_level_input = input('> ').lower()
        if tip_level_input == 'bad':
            return .1
        elif tip_level_input == 'fair':
            return .15
        elif tip_level_input == 'good':
            return .20
        else:
            print('\nInvalid input, please type \'bad\' \'fair\' or \'good\'')
        

def tip_calc():
    print('What was the bill amount?')
    bill = checks_if_float()
    percentage = tip_level()
    return round(bill * (1.00 + percentage), 2)

# print(f'Your total bill is: ${tip_calc()}')

# Tip calculator 2
# Same as the normal tip calc, but this time we ask how many people
# Will be splitting the bill
def checks_if_int():
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('\nInvalid input, please enter an integer')


def tip_calc_2():
    print('What was the bill amount?')
    bill = checks_if_float()
    percentage = tip_level()
    print('Total number of people?')
    people = checks_if_int()
    return round((bill * (1.00 + percentage))/people, 2)

# print(f'Total split bill for each person is: ${tip_calc_2()}')

# How many Coins?
# Counts how many coins, if you say you don't want another coin then the program ends
def how_many_coins():
    coins = 0
    while True:
        print(f'You have {coins} coins.\nDo you want another? (y or n)')
        answer = input('> ').lower()
        if answer == 'y':
            coins += 1
        elif answer == 'n':
            print('BYE NOW')
            return
        else:
            print('Not a valid choice...starting over\n')

# how_many_coins()

# Print a box
# Ask the user for a height and width
# Given their inputs (considering they are in fact valid), print out a box with the specifications
def build_a_box():
    print('Width? (int)')
    width = checks_if_int()
    print('Height? (int)')
    height = checks_if_int()
    i, string = 0, ''
    while i < height:
        if i == 0 or i == height - 1:
            string += '*' * width + '\n'
        else:
            string += '*' + ' ' * (width - 2) + '*\n'
        i += 1
    print(string)

# build_a_box()

# Print a triangle
# Given a height, print a triangle using *
def build_a_triangle():
    print('Triangle height? (int)')
    height = checks_if_int()
    i, stars, string = 1, 1, ''
    while i <= height:
        spaces = (height - i)
        string += ' ' * spaces + '*' * stars + '\n'
        i += 1
        stars += 2
    print(string)

# build_a_triangle()

# Multiplication Table
# Prints the multiplication table for numbers from 1 up to 10
def mult_table():
    print('Ending number for multiplication table? (int)')
    start = checks_if_int()
    outer = 1
    while outer <= start:
        inner = 1

        while inner <= start:
            print(f'{outer} X {inner} = {outer * inner}')
            inner += 1

        outer += 1

# mult_table()

def mult_table2():
    print('Ending number for multiplication table? (int)')
    end = checks_if_int()
    left, right = 1, 1
    while left <= end:
        print(f'{left} X {right} = {left * right}')
        left = left if right < end else left + 1
        right = right + 1 if right < end else 1

# mult_table2()
