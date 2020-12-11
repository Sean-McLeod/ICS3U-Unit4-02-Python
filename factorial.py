#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can do factorial


def main():
    # this function can tell the user the total multiplied number

    loop_counter = 1
    product = 1

    print("This program can multiply up from 1 to the number you type.")
    print("For example, 5: 1x2x3x4x5=120")
    print("\n", end="")

    # input
    positive_integer_string = input("Enter in a positive integer: ")
    print("\n", end="")

    # process & output
    try:
        positive_integer = int(positive_integer_string)

        if positive_integer == 0:
            print("The factorial of 0 is 1")
        else:
            if positive_integer > 0:
                while loop_counter <= positive_integer:
                    product = product * loop_counter
                    loop_counter = loop_counter + 1

                print("The multiplication of numbers from 1 to {0} is {1}"
                      .format(positive_integer, product))
            else:
                print("This is a negative integer")

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
