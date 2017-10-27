'''
This script generate summation and subtraction with negative numbers problems.

Ex.:

-23 + 4
-12 - 5
'''

import random

PROBLEMS_COUNT = 50


for i in range(PROBLEMS_COUNT):
    print('{}{} {} {} ='.format(
        random.choice(['', '-']),
        random.randint(3, 45),
        random.choice(['+', '-']),
        random.randint(3, 45))
    )
