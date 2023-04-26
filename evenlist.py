def list_even(x):
    even=[]
    for n in x:
        if (int(n)%2)==0:
            even.append(n)
    return even        
num= input("Enter list of integers : ")
x= num.split(" ")
print("Even numbers in list are : ",list_even(x))