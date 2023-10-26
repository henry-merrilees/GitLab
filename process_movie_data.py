#! /usr/bin/env python3
# A script that imports movie data and finds the top-5 highest grossing movies
import csv


def find_top_N(filename, n=10):
    """Finds the top n highest grossing movies in a CSV dataset.
       Input: filename, a string - points to filename of dataset
       Output: None
       Effect: should print n lines of text
    """
    # read in file contents as list of dictionaries
    with open(filename) as f:
        csvr = csv.DictReader(f)
        rows = [r for r in csvr]
    
    # Reformat some data types
    for row in rows:
        row["Gross"] = int(row["Gross"])
        row["Year"] = int(row["Release Date"][:4])

    # Sort data and get top 5
    gross_sort = lambda x : x["Gross"]
    rows.sort(key=gross_sort)
<<<<<<< HEAD
    top_n = rows[:-n-1:-1]

    # Print out results
    for i, row in enumerate(top_n):
=======
    top_ten = rows[:-11:-1]

    # Print out results
    for i, row in enumerate(top_10):
>>>>>>> 8b7440a (top_ten)
        print("{ind}. {row[Title]} ({row[Year]}) - ${row[Gross]:,d}".format(
            ind=i+1,
            row=row))


# Script to run
# Movie data comes from "Movie Gross and Ratings" dataset on Kaggle by Yashwanth Sharaf
# https://www.kaggle.com/datasets/thedevastator/movie-gross-and-ratings-from-1989-to-2014
if __name__ == "__main__":
<<<<<<< HEAD
    find_top_N("Movies_gross_rating.csv")
=======
    find_top_10("Movies_gross_rating.csv")
>>>>>>> 8b7440a (top_ten)
