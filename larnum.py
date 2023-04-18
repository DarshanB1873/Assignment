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
num1 = int(input("Enter first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if(num1>= num2) and (num >=num3):
    largest=num1
elif(num2>=num1) and (num2>=num3):
    largest=num2
elif(num3>=num2) and (num3>=num1):
    largest=num3
    print("largest no is",largest)


