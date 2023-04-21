#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darshan
#
# Created:     21-04-2023
# Copyright:   (c) Darshan 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#program to detect palindrome
a=int(input("Enter any number"))
b=a
rev=0
while(a>0):
    c=a%10
    rev=rev*10+c
    a=a//10
if(b==rev):
    print("Entered number is palindrome")
else:
    print("Entered no is not palindrome")