import requests
import random

def cat():
    url = 'https://cat-fact.herokuapp.com/facts'
    cat = requests.get(url).json()
    cat_facts = []
    for meow in cat:
        cat_facts.append(meow.get("text"))
    return f"{random.choice(cat_facts)}"




