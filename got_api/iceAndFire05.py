#!/usr/bin/python3
"""Alta3 Research - RZFeeser 
   SOLUTION 01 - Returning names to house and books with GOT API."""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def find_char(got_list):
    names=[]
    for x in got_list:
        res = requests.get(x)
        data = res.json()
        names.append(data.get('name'))
    return names


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        # call our function
        print("This character belongs to the following houses:")
        for x in find_char(got_dj.get("allegiances")):
            print(x)

        print("This character appears in the following books:")
        for x in find_char(got_dj.get("books")):
            print(x)

if __name__ == "__main__":
    main()