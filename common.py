a=str(input("Enter the string: "))
print("The original string is: ",a)
common_char={}
for i in a:
    if i in common_char:
        common_char[i]+=1
    else:
        common_char[i]=1
result=max(common_char,kay=common_char.get) 
print("The max of all characters is: "+str(result))           