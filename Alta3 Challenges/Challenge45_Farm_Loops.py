#!/usr/bin/env python3

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


yuck= ["carrots", "celery"]
NE_animals= farms[0]["agriculture"]
W_animals= farms[1]["agriculture"]
SE_animals= farms[2]["agriculture"]

user= input("Choose a farm (NE Farm, W Farm, SE Farm: ")
if user == "NE Farm":
    print(NE_animals)
elif user == "W Farm":
    print(W_animals)
elif user == "SE Farm":
    print(SE_animals)
      