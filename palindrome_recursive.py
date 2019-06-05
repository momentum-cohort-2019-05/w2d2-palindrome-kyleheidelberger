# get input from user
initial_input = input("""Input some text. It can be a phrase, a sentence, or multiple sentences. """)

# remove capitals, spaces, and punctuation
user_input = ""
user_input = initial_input

import re
user_input = re.sub(r'[^A-Za-z]', "", user_input)
user_input = user_input.lower()

#  recursion...

def palindrome(text):
    """Finds whether text is a palindrome or not."""
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        text = text[1:-1]
        return palindrome(text)

# print result
is_a_palindrome = palindrome(user_input)
if is_a_palindrome:
    print(initial_input, "is a palindrome.")
else:
    print(initial_input, "is not a palindrome.")