import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

codes_dictionary = {row.letter: row.code for (_, row) in df.iterrows()}
# print(codes_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
done = False
while not done:
    try:
        user_word = input("A word you want to get the phonetic codes of: ")
        user_word_codes = [codes_dictionary[letter.upper()] for letter in user_word]
        print(user_word_codes)
    except KeyError as k:
        print("Sorry, only letters in the alphabet please.")
    else:
        done = True
