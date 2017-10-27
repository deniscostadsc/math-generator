'''
This script generate very simple rule of three problems.

Ex.:

13   X
-- = ---
8    64


9    36
-- = ---
17   X

'''

import random

PROBLEMS_COUNT = 50

for i in range(PROBLEMS_COUNT):
    dividend = random.randint(7, 20)
    divisor = random.randint(7, 20)
    mul = random.randint(3, 9)
    len_dividend = len(str(dividend))
    len_divisor = len(str(divisor))

    randomic = random.randint(1,4)

    print('\n')
    if randomic == 1:
        print('X{}{}\n-- = ---\n{}{}{}'.format(
            ' ' * 4,
            dividend * mul,
            divisor,
            ' ' * (5 - len_divisor),
            divisor * mul)
        )
    elif randomic == 2:
        print('{}{}X\n-- = ---\n{}{}{}'.format(
            dividend,
            ' ' * (5 - len_dividend),
            divisor,
            ' ' * (5 - len_divisor),
            divisor * mul)
        )
    elif randomic == 3:
        print('{}{}{}\n-- = ---\nX{}{}'.format(
            dividend,
            ' ' * (5 - len_dividend),
            dividend * mul,
            ' ' * 4,
            divisor * mul)
        )
    else:
        print('{}{}{}\n-- = ---\n{}{}X'.format(
            dividend,
            ' ' * (5 - len_dividend),
            dividend * mul,
            divisor,
            ' ' * (5 - len_divisor))
        )
