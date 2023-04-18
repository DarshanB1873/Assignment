#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darshan
#
# Created:     18-04-2023
# Copyright:   (c) Darshan 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

year=int(input("Enter the year"))
if(year % 4)==0:
  print("{0} is leap year".format(year))
else:
  print("{0}is not a leap year".format(year))
