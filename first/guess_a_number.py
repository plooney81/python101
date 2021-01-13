import random

# game for guessing a number
def guessing_game():

    # this is function simply for checking if the user inputted an integer, if they don't, it will
    # ask continuely until an integer is inputted.
    def is_it_a_integer():
        while True:
            try:
                #we do not need a break here because return automatically ends a function and
                # returns the value of whatever is following the return keyword
                return int(input('> '))
                
            except ValueError:
                print('\nInvalid input, please input a integer and try again')

    # function that asks the user if it would like to play another round of the game, if no then it returns no
    # if yes, then it returns the string yes
    def continue_playing():
        print('would you like to play again (yes or no)?')
        while True:
            user_play_again = input('> ').lower()
            if user_play_again == 'yes':
                return 'yes'
            elif user_play_again == 'no':
                return 'no'
            else:
                print('Invalid input please enter either yes or no')

    # initiate a variable for the magic number
    # this is initiated with a random number between 1 and 10
    # random.randint(a,b) returns a random integer that is between a and b
    magic_number = random.randint(1, 10)

    # as the user how many guesses they would like
    print('\n\nHow many guesses would you like to have?')

    #checks to see if the using inputed an integer for the previous question, if they did, then it returns the value and 
    # it is saved into our variable numb_guesses, if they didn't input a variable, then it will continue to loop in the 
    # function until the user does input a variable
    numb_guesses = is_it_a_integer()

    # prompt the user to input a guess for the magic number
    print('\n\nInput an initial guess for the magic number')

    # calls a function to check if the value is an integer, if its not, then it will continuely ask again
    # until an integer is inputted.
    user_input = is_it_a_integer()

    # we need a counter variable for our while loop
    counter = 0

    # only way to get out of the loop is to guess the right number
    while counter < (numb_guesses):

        #we need to iterate the counter variable
        counter += 1
        
        # if the user guesses right and wants to continue playing, then the while loop will break
        if user_input == magic_number:
            print('Congratulations, you guessed right!')
            # the response to the function is saved in the var resp
            resp = continue_playing()
            # if resp is 'no' i.e. the playing wants to quit playing, then we break the function
            if resp == 'no':
                break
            # if the resp is 'yes' then the playing wants to play another round so we call the entire 
            # game again and then break after so it this current while loop we are in, doesn't just keep looping, 
            # basically it starts the entire game over again
            elif resp == 'yes':
                guessing_game()
                break
        
        # if the guess isn't the magic number, and is too low, then the user is told so, and is prompted to guess again
        # by calling the is_it_a_integer function again, the return of that function is then saved back into the user
        # input variable and then the while loop starts over again
        elif user_input < magic_number:
            print(f'\n{user_input} is too low, you have {numb_guesses - (counter)} guesses left')

        
        # if the guess isn't the magic number, and is too high, then the user is told so, and is prompted to guess again
        # by calling the is_it_a_integer function again, the return of that function is then saved back into the user
        # input variable and then the while loop starts over again
        elif user_input > magic_number:
            print(f'\n{user_input} is too high, you have {numb_guesses - (counter)} guesses left')
        
    


        # after we iterate the number variable, if it equals the number of guesses, then the while loop will terminate and the game will be over
        if counter == (numb_guesses):
            print('You ran out of guesses')
            resp = continue_playing()
            # if resp is 'no' i.e. the playing wants to quit playing, then we break the function
            if resp == 'no':
                break
            # if the resp is 'yes' then the playing wants to play another round so we call the entire 
            # game again and then break after so it this current while loop we are in, doesn't just keep looping, 
            # basically it starts the entire game over again
            elif resp == 'yes':
                guessing_game()
                break
        else:
            print('\nTry again')
            # capture the new user input
            user_input = is_it_a_integer()

# have to call the game function initially to start off the game or else nothing would happen
guessing_game()