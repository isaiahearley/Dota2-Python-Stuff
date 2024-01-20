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


#function to randomize support heroes
def support_low_prio():
    filtered_support_data = [hero['localized_name'] for hero in data if 'Support' in hero['roles']]
    support_hero_amt = len(filtered_support_data)

    #stored support values
    support_value1 = random.randint(0, support_hero_amt)
    support_value2 = random.randint(0, support_hero_amt)
    support_value3 = random.randint(0, support_hero_amt)

    #print(support_hero_amt)
    #print(filtered_support_data)
    
    print("\nSupport Randomizer")
    print(f"\nYour options are {filtered_support_data[support_value3]}, {filtered_support_data[support_value2]} and {filtered_support_data[support_value1]}!\n")
    
support_low_prio()


def carry_low_prio():
    filtered_carry_data = [hero['localized_name'] for hero in data if 'Carry' in hero['roles']]
    carry_hero_amt = len(filtered_carry_data)
    
    #stored carry values
    carry_value1 = random.randint(0, carry_hero_amt)
    carry_value2 = random.randint(0, carry_hero_amt)
    carry_value3 = random.randint(0, carry_hero_amt)
    
    #print(carry_hero_amt)
    #print(filtered_carry_data)
    print("\nCarry Randomizer")
    print(f"\nYour options are {filtered_carry_data[carry_value3]}, {filtered_carry_data[carry_value2]} and {filtered_carry_data[carry_value1]}!\n")

carry_low_prio()

#function to randomize 3 values for low prio
def lowprio():
    filtered_hero_data = [hero['localized_name'] for hero in data if hero.get('localized_name')]
    #get length of list and randomize values between 0 / heroamt
    hero_amt = len(filtered_hero_data)

    #stored values
    value1 = random.randint(0, hero_amt)
    value2 = random.randint(0, hero_amt)
    value3 = random.randint(0, hero_amt)

    #result for user
    print("\nAll Randomizer")
    print(f"\nYour options are {filtered_hero_data[value3]}, {filtered_hero_data[value2]} and {filtered_hero_data[value1]}!\n")
    

lowprio()



#return carry / support / all depending on what user wants
