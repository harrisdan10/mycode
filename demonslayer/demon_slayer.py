#!/usr/bin/env python3

round = 0 

while True:
    round += 1
    print('Finish the following statement: "Tanjiro Kamado is a practictioner of the _____ breathing style"')
    answer = input("Your answer --> ").lower()

    if answer == "water":
        print("🌊🌊🌊 Correct!")
        break;
    elif answer == "hinokami kagura":
        print("☀☀ You gave the super secret answer!!")
        break;
    elif round == 3:
        print("Sorry, the correct answer was water.")
        break;
    else:
        print(f"Sorry! Try again! You have {3 - round} chance(s) remaining!")
