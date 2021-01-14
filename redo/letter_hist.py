# Function that takes a string from the user, and then prints a dictionary containing the tally of how many 
# times each letter in the alphabet was used in the word
def letter_hist(str):
    letter_hist = {}
    for char in str:
        char = char.lower()
        if char != ' ':
            letter_hist[char] = letter_hist[char] + 1 if (char in letter_hist) else 1

    print(letter_hist)

letter_hist('Peter Looney')