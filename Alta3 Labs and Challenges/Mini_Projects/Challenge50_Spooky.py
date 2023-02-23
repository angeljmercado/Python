#!/usr/bin/env python3
vampire= 0
with open("dracula.txt", "r") as d_txt:
    for line in d_txt:
        if "vampire" in line.lower():
            with open("vampytimes.txt", "a") as vfile:
                vfile.write(line)

           
