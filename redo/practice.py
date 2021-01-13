# print("What is this \"pancakes\" you speak of")
# food = 'pancakes'
# print(f'What is this "{food}" you speak of')
# print(f"What is this '{food}' you speak of")
# print(f'''What is this '{food}' you speak of''')
# print(len(f'''What is this `{food}` you speak of'''))

# print("whats up %s, you look %s today" %('10', 'wonderful'))
user_input = int(input('Enter a number'))
if user_input == 0 or user_input == 6:
    print('Sleep in, its the weekend')
elif user_input < 0 or user_input > 6:
    print('Invalid please try again')
else:
    print('Go to work')