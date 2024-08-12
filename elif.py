import math
import os
import random
import re
import sys

def check_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and n in range(2,6):
        return "Not Weird"
    elif n % 2 == 0 and n in range(6,21):
        return "Weird"
    elif n % 2 == 0 and n in range(20,101):
        return "Not Weird"

if __name__ == '__main__':
 n = int(input("enter a number"))
 result = check_weird(n)
 print(result)