from name_converter import invite_names

name_list = invite_names

with open("Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
for name in name_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        new_letter = letter.replace("[name]", name)
        file.write(new_letter)
