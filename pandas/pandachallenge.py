#!/usr/bin/env python3

import pandas

def main():

    data_frame = pandas.read_csv("5movies.csv")

    data_frame.drop(data_frame.columns.difference(["Title", "Year", "Budget"]), 1, inplace=True)

    data_frame.to_json("secondary_5movies.json")

    json_file = "secondary_5movies.json"

    json_movies = pandas.read_json(json_file)

    print(json_movies.head())

if __name__ == "__main__":
    main()