"""
Create a function named isAnagram() following your current language's style guide.
 It should take two strings and return a boolean value depending on whether it's an anagram or not.

input 1	  input 2	output
"dog"	   "god"	  true
"green"	   "fox"	  false


"""
print("Enter two words to check anagram!")
word_1 = input("Enter word one: ").lower()
word_2 = input("Enter word two: ").lower()

def isAnagram(word_1, word_2):    
    if len(word_1) != len(word_2):
        return False
    
    return sorted(word_1) == sorted(word_2)



print(isAnagram(word_1, word_2))