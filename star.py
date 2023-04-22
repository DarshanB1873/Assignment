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

def starp1(n):

    for i in range(1, n+1):

        for j in range(1, i + 1):
            print("* ", end="")
        print()

n = int(input("Enter number of rows:"))
starp1(n)