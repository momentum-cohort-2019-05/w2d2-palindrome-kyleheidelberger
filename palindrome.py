# get input from user
initial_input = input("""Input some text. It can be a phrase, a sentence, or multiple sentences. """)

# remove capitals, spaces, and punctuation
user_input = ""
user_input = initial_input

#  this is the initial way I did it before seeing the notes...

# print("Removing capital letters...")
# user_input = user_input.lower()
# print("Removing spaces...")
# user_input = user_input.replace(" ", "")
# print("Removing punctuation...")
# user_input = user_input.replace(".", "")
# user_input = user_input.replace(",", "")
# user_input = user_input.replace("!", "")
# user_input = user_input.replace(":", "")

import re
user_input = re.sub(r'[^A-Za-z]', "", user_input)
user_input = user_input.lower()

print("Determining if your input is a palindrome...")

# determine if string is a palindrome
if user_input == user_input[::-1]:
    print(initial_input, "is a palindrome.")
else:
    print(initial_input, "is not a palindrome.")

# alternate way? not sure if needed to define a function or not

# # determine if string is a palindrome
# def palindrome(initial_input):
#     if user_input == user_input[::-1]:
#         print(initial_input, "is a palindrome.")
#     else:
#         print(initial_input, "is not a palindrome.")
# 
# palindrome(initial_input)
