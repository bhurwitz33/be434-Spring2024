#!/usr/bin/env python3
"""
Author : Roberta Gracia
Date   : 2024-02-02
Purpose: Sums numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sums numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start here"""

    args = get_args()

    total = 0
    myList = []
    for i in args.numbers:
        total += i
        myList.append(str(i))

    line = " + ".join(myList)
    str(total)
    print(f'{line} = {total}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

