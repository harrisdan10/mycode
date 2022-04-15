from dict import working

start= "q1"

while start != "end":
    print(working[start]["question"])
    answer= input(">").lower().strip()
    if answer in ["yes","no"]:
        start = working[start][answer]
    else:
        print("Please choose yes or no.")
