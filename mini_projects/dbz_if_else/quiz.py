#!/usr/bin/env python3

import os
from characters import chars

questions = ["How would you describe yourself? \n A. prideful \n B. charasmatic \n C. loyal \n D. devious \n", 
"How would your friends best describe you? \n A. funny \n B. sarcastic \n C. vengeful \n D. determined \n E. I have no friends \n",
"How important is winning to you? \n A. It's everything \n B. I'm in it for the challenge\n C. It couldn't care less about winning \n",
"How do you spend your free time? \n A. eating/sleeping \n B. working out \n C. studying \n D. gaming \n",
"What is your preferred movie/tv genre? \n A. Comedy \n B. Romance \n C. Horror \n D. Action \n"]

i = 0

def ask_questions():
    global i
    for question in questions:
        answer = ""
        while answer == "" or answer not in ["A", "B", "C", "D", "E"]:
            answer = input(question).upper()
            values(i, question, answer)

def values(i, question, answer):
    if question == questions[i]:
        if answer == "A":
            chars["Goku"] += 1
            chars["Vegeta"] += 1
            chars["Frieza"] += 1
        elif answer == "B":
            chars["Goku"] += 1
        elif answer == "C":
            chars["Krillin"] += 1
        elif answer == "D":
            chars["Frieza"] += 1
            chars["Vegeta"] += 1
        else: 
            print(f"{answer} is not valid for this question. I see you're a rebel")
            chars["Frieza"] += 1
            chars["Vegeta"] += 1          

    if question == questions[i]:
        if answer == "A":
            chars["Goku"] += 1
        elif answer == "B":
            chars["Vegeta"] += 1
            chars["Frieza"] += 1
        elif answer == "C":
            chars["Vegeta"] += 1
            chars["Frieza"] += 1
        elif answer == "D":
            chars["Goku"] += 1
            chars["Krillin"] += 1
        else:
            chars["Frieza"] += 1

    if question == questions[i]:
        if answer == "A":
            chars["Vegeta"] += 1
            chars["Frieza"] += 1
        elif answer == "B":
            chars["Goku"] += 1
        elif answer == "C":
            chars["Frieza"] += 1
        else:
            print(f"{answer} is not valid for this question. I see you're a rebel")
            chars["Frieza"] += 1
            chars["Vegeta"] += 1

    if question == questions[i]:
        if answer == "A":
            chars["Goku"] += 1
        elif answer == "B":
            chars["Goku"] += 1
            chars["Vegeta"] += 1
        elif answer == "C":
            chars["Krillin"] += 1
        elif answer == "D":
            chars["Frieza"] += 1
        else: 
            print(f"{answer} is not valid for this question. I see you're a rebel")
            chars["Frieza"] += 1
            chars["Vegeta"] += 1

    if question == questions[i]:
        if answer == "A":
            chars["Goku"] += 1
        elif answer == "B":
            chars["Krillin"] += 1
        elif answer == "C":
            chars["Frieza"] += 1
        elif answer == "D":
            chars["Vegeta"] += 1
        else: 
            print(f"{answer} is not valid for this question. I see you're a rebel")
            chars["Frieza"] += 1
            chars["Vegeta"] += 1
    i += 1
    os.system("clear")
    
ask_questions()

find_char = max(chars, key=chars.get)
print(f"Love it or hate it, you are most like {find_char}")

