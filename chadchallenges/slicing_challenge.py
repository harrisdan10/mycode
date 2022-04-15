#!/usr/bin/env python3
import itertools

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes = [challenge[2][1], trial[2]["goggles"], nightmare[0]["user"]["name"]["first"]]
goggles = [challenge[2][0], trial[2]["eyes"], nightmare[0]["kumquat"]]
nothing = [challenge[3], trial[3], nightmare[0]["d"]]

for (eye, goggle, nada) in zip(eyes, goggles, nothing):
    print(f'My {eye}. The {goggle} do {nada}!')


