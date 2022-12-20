#!/usr/bin/python3

"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    param = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
