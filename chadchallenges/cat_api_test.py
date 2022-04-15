from cat_api import cat

def test_cat():
    assert cat() in ["Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.", "Cats make about 100 different sounds. Dogs make only about 10.", "I don't know anything about cats.", "The technical term for a cat’s hairball is a bezoar.", "Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs."]