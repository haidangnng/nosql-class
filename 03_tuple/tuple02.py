#!/usr/bin/env python3

import math


def distance(p1, p2):
    # TODO...
    return math.dist(p1, p2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print("The distance between the two points:", distance(p1, p2))


############################################################################

if __name__ == "__main__":
    main()
