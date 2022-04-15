import requests

url = "https://pokeapi.co/api/v2/pokemon/1"

# response = requests.get(url)

# print(dir(response))
# print(response.json())

response = requests.get(url).json()

# for poke_dict in response["moves"]:
#     print(poke_dict["moves"]["name"])