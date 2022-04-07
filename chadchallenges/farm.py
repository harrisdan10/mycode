farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


farm_animals = farms[0].get("agriculture")
for animal in farm_animals:
    print(animal)

user_input = input("Choose a farm (NE, W, SE, East, West): ").lower()
for farm in farms:
    if farm["name"].lower() == user_input + " farm":
        print(farm.get("agriculture"))

scrap = ["carrots", "celery", "apples", "oranges"]

for farm in farms:
    if farm.get("name").lower() == user_input + " farm":
        for agri in farm.get("agriculture"):
            if agri not in scrap:
                print(agri)



