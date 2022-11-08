#!/usr/bin/env python3
# Created by: Katie G
# Created on: November 7th, 2022
# This program asks the user for a number
# to turn into a factorial,
# then uses a try...catch statement to determine
# if the user's number is valid, then uses an if
# else statement to check if the user's num is positive,
# then, uses a do...while loop to loop the program
# while multiplying the factorial by the loop counter
# until the factorial is calculated and the loop counter
# is equal to the user input.


# this function gets the user number, then
# uses try...catch, if...else statements
# and a do...while loop to get the factorial
# from the user.
def main():
    # initializing the factorial and loop counter variables.
    loop_counter = 0
    factorial = 1
    # getting user input on what number they want
    # the factorial of
    user_num_as_string = input(
        "Hello! It is time for factorials. If you have a problem with this, "
        "please contact your local Cyberlife representative. Give me your desired "
        "number so i can turn it into a factorial :D "
    )

    # uses a try...catch statement to determine
    # if the user's number is a valid integer.
    try:
        user_num_as_int = int(user_num_as_string)
        if user_num_as_int >= 0:
            while True:
                loop_counter = loop_counter + 1
                factorial = factorial * loop_counter
                if loop_counter >= user_num_as_int:
                    print(
                        "The factorial of {} is {}".format(user_num_as_int, factorial)
                    )
                    break
        else:
            print(
                "Sorry, this is not a valid input! "
                "Please input a whole integer greater than or equal to zero."
            )
    except Exception:
        print(
            "Sorry, this is not a valid input! "
            "Please input a whole integer greater than or equal to zero."
        )
    finally:
        print("Cyberlife thanks you for using this program.")


if __name__ == "__main__":
    main()
