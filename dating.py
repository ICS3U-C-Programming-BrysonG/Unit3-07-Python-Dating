#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 10 22, 2026
# This program gets the users age and checks if they are eligible to date
# the grandparents grandchild.


import constants


def main():
    age_user_as_string = input("Enter your age: ")

    # See if their age is eligible
    try:
        age_user_int = int(age_user_as_string)
        try:
            if age_user_int < 0:
                0 / 0
        except:
            print("A negative number is not a valid age")
        try:
            if age_user_int > 120:
                0 / 0
        except:
            print("No human can live that long")
        if age_user_int > constants.MINAGE and age_user_int < constants.MAXAGE:
            print("You are eligible!")
        else:
            print("You are not eligible for my grandchild")
    except:
        print("{} is not a valid age".format(age_user_as_string))


if __name__ == "__main__":
    main()
