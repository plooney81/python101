# Program that asks how many coins the user wants

# initiate our coin counter variable at 0
coin_counter = 0

# while loop that will stay true until the user inputs no
while True:

    # shows the user our current amount of coins
    if coin_counter == 0:
        print(f'\nYou currently don\'t have a single coin')
    elif coin_counter == 1:
        print(f'\nYou only have {coin_counter} coin')
    else:
        print(f'\nYou have {coin_counter} coins')
    
    print('Would you like to add a coin (yes or no)?')
    # converts the user input to lower case so we can evaulate against only the yes
    # or no cases, versus if the user inputted YeS or YES or yEs or No or NO or nO, etc.
    user_input = input('> ').lower()

    if user_input == 'yes':
        # if they want another coin then we add one to the coin counter
        coin_counter = coin_counter + 1
    elif user_input == 'no':
        # if they dont want any more coins then it will break the while loop and exit
        # the program
        print('Bye')
        break
    else:
        # if the input isn't yes or no, they it will loop and continue to ask for an input until a valid input is given
        print('\nInvalid input, please input either yes or no')