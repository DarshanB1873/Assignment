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

s=str(input("Enter any string :"))
count=0
for i in range(0,len(s)):
    if(s[i]!=''):
        count=count+1
print("Numbers of characters in string: "+str(count))