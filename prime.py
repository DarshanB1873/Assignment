#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darshan
#
# Created:     20-04-2023
# Copyright:   (c) Darshan 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1=int(input("Enter the lower range"))
num2=int(input("Enter the upper range "))
print("prime number between",num1,"and",num2,"are :")
for n in range(num1,num2 + 1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)