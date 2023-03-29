"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as 
forward, such as madam or racecar. [for more detail check palindrome on Wikipedia].

Create a function named createPalindrome() following your current language's style guide. 
It should take a string, create a palindrome from it and then return it.

Examples input output "" "" "greenfox" "greenfoxxofneerg" "123" "123321"

"""

def createPalindrome(the_word):
    the_word_length = len(the_word)
    inverted_word=""
    for i in range(1, the_word_length + 1):
        inverted_word += the_word[-i]
    
    return the_word + inverted_word
    


print(createPalindrome("greenfox"))

