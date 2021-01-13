# Prompt the user to enter their name
print('Please enter your name below')

# save the input to a variable name user_name and then change that to all upper case
user_name = input('> ')

#print the upper case version of the user name
print(f'Here is your name all in upper case: {user_name.upper()}. How cool is that ?\nAlso your name has {len(user_name)} letters in it.')
