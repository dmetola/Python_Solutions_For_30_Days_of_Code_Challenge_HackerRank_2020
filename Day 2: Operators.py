#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    cal_tip = meal_cost * tip_percent / 100
    cal_tax = meal_cost * tax_percent / 100
    totalCost = meal_cost + cal_tip + cal_tax
    print(str(round(totalCost)))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())
    
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
