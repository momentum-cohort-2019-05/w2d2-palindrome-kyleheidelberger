# to determine if same forwards and backwards, iterate through it recursively or using loop

# get input from user
initial_input = input("""Input some text. It can be a phrase, a sentence, or multiple sentences. """)

# remove capitals, spaces, and punctuation
user_input = ""
user_input = initial_input

import re
user_input = re.sub(r'[^A-Za-z]', "", user_input)
user_input = user_input.lower()

print("Determining if your input is a palindrome...")

# determine if string is a palindrome
if user_input == user_input[::-1]:
    print(initial_input, "is a palindrome.")
else:
    print(initial_input, "is not a palindrome.")

