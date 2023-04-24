st=str(input("Enter any string: "))
vowels=['a','e','i','o','u','A','E','I','O','U']
remove_vowel=""
for i in range(len(st)):
    if st[i]not in vowels:
        remove_vowel=remove_vowel+st[i]
print("String after removing vowel is: ",remove_vowel)        