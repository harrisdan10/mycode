#!/usr/bin/env python3
import requests
import random

url = "https://cat-fact.herokuapp.com/facts"

def main():

    res = requests.get(url).json()

    cat_facts=[]

    for cat_dict in res:
        print(cat_dict["text"])

        cat_facts.append(cat_dict["text"])

    random_fact = random.choices(cat_facts)
    print(random_fact)
    
if __name__ == "__main__":
    main()
