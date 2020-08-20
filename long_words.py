# give a word as a user input, print the result of extending any long vowels to the length of 5.
# so if the user inputs the word good then it will change to --> goooood

# long vowels = a, e, i, o, u

# prompt the user for input
print('\nPlease enter a word')

# while loop to see if the user entered a string or not
while True:
    try:
        user_input = input('> ')
        is_string = int(user_input)
        print('\nInvalid input, please enter a string')
    except ValueError:
        break

# convert it to lowercase for our if statement below (except for the first letter)
user_input = user_input[0] + user_input[1:].lower()

# counter variable
counter = 0

# variable that contains the length of the string inputted
length_of_string = len(user_input)

# for loop to go through each letter in the word the user has inputted.
for characters in user_input:
    # initiate a boolean var called is a vowel, will be true if a character is a vowel
    is_vowel = (characters == 'a' or characters == 'e' or characters == 'i' or characters == 'o' or characters == 'u')

    # we don't want any of the leading characters or last characters to be changed even if it is a vowel
    if is_vowel and (counter != 0 or counter != (length_of_string - 1)):
        user_input = user_input.replace(characters, characters * 5, 1)

# print the new word with replaced vowels
print(user_input)