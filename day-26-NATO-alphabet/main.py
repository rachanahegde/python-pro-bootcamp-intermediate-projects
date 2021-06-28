import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
letters_list = list(word)
phonetic_list = [phonetic_dict[letter] for letter in letters_list]
print(phonetic_list)

