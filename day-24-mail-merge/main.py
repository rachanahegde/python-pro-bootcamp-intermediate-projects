with open("./Input/Letters/starting_letter.txt") as letter:
    basic_letter = letter.read()

with open("./Input/Names/invited_names.txt") as recipients:
    original_list = recipients.readlines()
    list_names = []
    for element in original_list:
        list_names.append(element.strip())

for name in list_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as birthday_letter:
        birthday_letter.write(basic_letter)

    birthday_letter = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "r")
    list_of_lines = birthday_letter.readlines()
    updated_lines = []
    for item in list_of_lines:
        item = item.replace("[name]", f"{name}")
        updated_lines.append(item.strip())
    for item in updated_lines[:1]:
        list_of_lines[0] = item

    birthday_letter = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    birthday_letter.writelines(list_of_lines)
    birthday_letter.close()


# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend".

# ------------------------ Alternative Solution --------------------------- #
# PLACEHOLDER = "[name]"
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

