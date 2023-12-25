import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("What is your name?").upper()
    try:
        new_list = [nato[n] for n in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()