# Madlib story
# These first couple of lines describe how the game works
print('Welcome to my madlib game!')
print('\nEnter in your answers for the following text')
print('\nWhere you see (name1) and then are later asked for a name for (name1), please enter a name')

# Variable for holding our madlib story
madlib_story = """One day (name1) was walking through the forest. They decided to go to (someplace1). 
Upon arriving to (someplace1) they looked around and shouted 'wow this place is (adjective1)'."""

# Print the story
print('\n\n' + madlib_story)

# prompt the user for name1
print('\nPlease enter below a name for the (name1) slot.')
user_input_answer1 = input('> ')

#prompt the user for someplace 1
print('\nPlease enter below a place for the (someplace1) slot.')
user_input_answer2 = input('> ')

#prompt the user for adjective 1
print('\nPlease enter a adjective for the (adjective1) slot.')
user_input_answer3 = input('> ')

# we need to change our madlib story
madlib_story = f"""One day {user_input_answer1} was walking through the forest. They decided to go to {user_input_answer2}. 
Upon arriving to {user_input_answer2} they looked around and shouted 'wow this place is {user_input_answer3}'."""

# and then we finally print our new madlib story
print('\n\nHere is your new story:\n\n' + madlib_story)