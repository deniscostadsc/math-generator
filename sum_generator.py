import random

PROBLEMS_COUNT = 50


for i in range(PROBLEMS_COUNT):
    print('{}{} {} {} ='.format(
        random.choice(['', '-']),
        random.randint(3, 45),
        random.choice(['+', '-']),
        random.randint(3, 45))
    )
