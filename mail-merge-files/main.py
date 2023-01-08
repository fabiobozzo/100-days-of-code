with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open("./Input/Names/invited_names.txt") as invited_names_file:
    invited_names = invited_names_file.readlines()
    for name in invited_names:
        new_letter = starting_letter.replace("[name]", name.strip())
        new_letter_file = open(f"./Output/ReadyToSend/letter_{name.lower()}.txt", mode="w")
        new_letter_file.write(new_letter)
        new_letter_file.close()
