#!/usr/bin/env python3

import html
from time import sleep
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question= html.escape(trivia["question"])
correct= html.escape(trivia["correct_answer"])
incorrect1= html.escape(trivia["incorrect_answers"][0])
incorrect2= html.escape(trivia["incorrect_answers"][1])
incorrect3= html.escape(trivia["incorrect_answers"][2])

print(question)
sleep(1)
print(f"A: {correct}")
sleep(0.5)
print(f"B: {incorrect1}")
sleep(0.5)
print(f"C: {incorrect2}")
sleep(0.5)
print(f"D: {incorrect3}")

