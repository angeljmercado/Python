#!/usr/bin/env python3

marvelchars = {
"Starlord":
  {"real name": "Peter Quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "Raven Darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "Bruce Banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
# Ask user for Character Input
char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk")
char_name.capitalize()
# Ask user for a specific statistic
char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy")

print(f"{char_name.capitalize()}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

