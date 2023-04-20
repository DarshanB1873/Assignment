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

#sum of all numbers from 1 to n divisible by 3

num=int(input("Enter the nth value for the range"))
def sum(a):
     sum=0
     for i in range(1,num):
      if i%3==0:
        sum+=i
     print(sum)
sum(num)