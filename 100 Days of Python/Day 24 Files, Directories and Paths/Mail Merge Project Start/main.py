PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names_list:
        stripped_names = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_names)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", "w") as out_letter:
            out_letter.write(f"{new_letter}")






f"{letter_contents}".replace(PLACEHOLDER, f"{name}")









    


        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp