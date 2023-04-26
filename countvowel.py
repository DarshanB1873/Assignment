string=str(input("Enter any string"))
def count_vowel(string):
    count=0
    vowel='a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    for alphabet in string:
        if alphabet in vowel:
            count=count+1
    print("Number of vowels in string are: ",count) 
count_vowel(string)           