import pandas
phonetic_table = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {
    row.letter: row.code for (index, row) in phonetic_table.iterrows()
}

user_word = input("Input a word: ")
print([phonetics[letter] for letter in user_word.upper()])
