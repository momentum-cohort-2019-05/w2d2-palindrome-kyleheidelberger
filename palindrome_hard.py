# get input from user
initial_input = input("""Input some text. It can be a phrase, a sentence, or multiple sentences. """)

# remove capitals, spaces, and punctuation
user_input = ""
user_input = initial_input

import re
user_input = re.sub(r'[^A-Za-z]', "", user_input)
user_input = user_input.lower()

# function to iterate to match first and last letter, then continue if match
def palindrome(text):
    """Determines whether or not inputted text is a palindrome."""
    is_a_palindrome = True
    
    i=0
    while is_a_palindrome and i<(len(text)/2):
        if text[i] != text[(i+1)*(-1)]:
            is_a_palindrome = False
        i += 1
    return is_a_palindrome

# print result
is_a_palindrome = palindrome(user_input)
if is_a_palindrome:
    print(initial_input, "is a palindrome.")
else:
    print(initial_input, "is not a palindrome.")