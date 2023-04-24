#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darshan
#
# Created:     24-04-2023
# Copyright:   (c) Darshan 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
m=int(input("Enter the marks: "))
if m>80:
    print("First class")
elif m<80 and m>=70:
    print("Second class")
elif m<70 and m>=60:
    print("Average")
elif m<60 and m>=40:
    print("Pass")
else:
    print("Fail")