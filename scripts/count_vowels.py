#taking input from the user
string = input("Enter a String : ")   
vowels = 0  #variable to count number of vowels
consonants = 0 #variable to count number of consonants
for i in string:  #string iteration 
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  #if character in string is vowel
        vowels+=1 #if vowel increment variable ‘vowel’ with one
    elif i.isalpha():  #checking if the character is alphabet
        consonants+=1  #if consonant increment variable ‘consonants’ with one
print("Vowels :",vowels,"Consonants:",consonants)
