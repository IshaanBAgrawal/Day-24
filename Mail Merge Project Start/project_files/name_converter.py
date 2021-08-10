with open("../project_files/Input/Names/invited_names.txt") as invited_people:
    invite = invited_people.read()
invite_name_letters = []
for char in invite:
    if char == '\n':
        pass
    else:
        invite_name_letters.append(char)

invite_names = []
name_char = []
for char in invite_name_letters:
    if char.isupper():
        name = ""
        for character in name_char:
            name += character
        invite_names.append(name)
        name_char = [char]
    elif char.islower():
        name_char.append(char)
last_name = ""
for last_name_chars in invite_name_letters[-4:]:
    last_name += last_name_chars
invite_names.append(last_name)
invite_names.pop(0)

uncle_name = f"{invite_names[-3]} {invite_names[-2]}"
invite_names.append(uncle_name)
invite_names.pop(-4)
invite_names.pop(-3)

