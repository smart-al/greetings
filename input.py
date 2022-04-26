#!/usr/bin/env python3

"""Basic Input Program For Name And Greeting"""

import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  print(f"hello {name}, your random number is {number}.")

greeting()
