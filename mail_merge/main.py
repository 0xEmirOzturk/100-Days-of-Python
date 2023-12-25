PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()


with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in all_names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)