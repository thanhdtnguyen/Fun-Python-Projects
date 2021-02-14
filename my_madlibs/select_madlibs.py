# randomize the collection of madlibs for players

from madlibs_collection import simple, business
import random

def main():
    select_madlib = random.choice([simple, business])
    select_madlib.madlib()

if __name__ == '__main__':
    main()

