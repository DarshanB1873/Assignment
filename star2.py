#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darshan
#
# Created:     22-04-2023
# Copyright:   (c) Darshan 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# define a function to print star shape
def star_pattern2(n):
    # Use outer for loop for rows

    for i in range(n, 0, -1 ):

        # Use inner for loop for columns / stars

        for j in range(1, i + 1):
            # print stars in each row
            print("* ", end="")

        # End of line after each row
        print()

n = int(input("Enter number of rows:"))
star_pattern2(n)