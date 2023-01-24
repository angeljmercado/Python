#!/usr/bin/env python3
import random

wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

#num= input("Choose a number between 1 and 20: ")
#num= int(num)

#student_name= tlgstudents[num]

student_name= random.choice(tlgstudents)
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]}")

