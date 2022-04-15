#!/usr/bin/env python3

import requests

def get_question():
    url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=boolean"
    resp = requests.get(url).json()
    return resp


