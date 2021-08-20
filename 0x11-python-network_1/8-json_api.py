#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import json
from requests import post, exceptions
from sys import argv

if (len(argv) == 2):
	payload = {"q":argv[1]}
else:
	payload = {"q":""}
response = post("http://0.0.0.0:5000/search_user", data=payload)
try:
	json_response = response.json()
	if (json_response):
		print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
	else:
		print("No result")
except:
	print("Not a valid JSON")
