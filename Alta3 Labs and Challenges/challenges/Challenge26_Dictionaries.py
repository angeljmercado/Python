#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

while True:

    char_name= input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").title()

    char_stat= input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

    if input("Want to choose again?") == "yes":
        continue
    else:
        break

