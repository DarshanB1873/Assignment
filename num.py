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
num=int(input("Enter the number :"))
add=0
for i in range (1,num):
    if(num%i==0):
        add=add+i
    if add==num:
        print("The number",num,"is a perfect number")
    else:
        print("the number",num,"is not perfect number")