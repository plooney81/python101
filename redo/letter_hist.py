# Function that takes a string from the user, and then prints a dictionary containing the tally of how many 
# times each letter in the alphabet was used in the word
# def letter_hist(str):
#     letter_hist = {}
#     for char in str:
#         char = char.lower()
#         if char != ' ':
#             letter_hist[char] = letter_hist[char] + 1 if (char in letter_hist) else 1

#     print(letter_hist)

# # letter_hist('Peter Looney')

# import pickle

# with open('heroes.txt', 'rb') as file_handle:
#     old_message = pickle.load(file_handle)
#     print(f'Old message is: "{old_message}"')

# user_input = input('What to save? ')

# with open('heroes.txt', 'wb') as file_handle:
#     contents = pickle.dump(user_input, file_handle)
#     # print(contents)

hist = {'to': 2, 'be': 3, 'or': 1, 'not':4}

def sorting_histogram(dictorionary):
    for word in sorted(dictorionary, key=dictorionary.get, reverse=True):
        print(word, dictorionary[word])

sorting_histogram(hist)