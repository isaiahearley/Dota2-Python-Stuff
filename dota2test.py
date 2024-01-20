# Name: Isaiah Earley
# Date: 1/18/24
# 
#
# Documentation for OpenDota API: https://pyopendota.readthedocs.io/en/latest/readme.html#features
# Installation: pip install pyopendota
#
# Synopsis: To my friends who always ask for hero suggestions to grief games lol

import opendota
import random

#initiates connection to OpenDota api
client = opendota.OpenDota()

#create empty list for data
data = []
data = client.search_hero()

#function to randomize 3 values for low prio
def lowprio():
    filtered_data = [hero['localized_name'] for hero in data if hero.get('localized_name')]
    #get length of list and randomize values between 0 / heroamt
    heroamt = len(filtered_data)

    #stored values
    value1 = random.randint(0, heroamt)
    value2 = random.randint(0, heroamt)
    value3 = random.randint(0, heroamt)

    #result for user
    print("\nLow Prio Simulator")
    print(f"\nYour options are {filtered_data[value3]}, {filtered_data[value2]} and {filtered_data[value1]}!\n")
    
#return function 
lowprio()

