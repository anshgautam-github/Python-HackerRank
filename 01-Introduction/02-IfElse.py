/**
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than , print Not Weird

*/

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n<=5 and n>=2:
        print("Not Weird")
    elif n<=20 and n>=6:
        print("Weird")
    else:
        print("Not Weird")
