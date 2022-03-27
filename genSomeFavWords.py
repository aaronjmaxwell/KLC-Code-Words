"""Set up the Cracking Codes.

Step 1: Get the students to build a new project.
Step 2: Have them print something!
Step 3: Have them generate lists of favourite words and characters.
Step 4: Have them pick a new random word, character, number. Import random!
Step 5: Have them join the three together and print!
Bonus: Have them shuffle the order.

@author: Bilal Qadar
@organization: Canada Learning Code
"""
__author__ = "AJMax"
__version__ = "1.0.0"
import random

print("Your new password is:")

favourite_words = ["orange", "cat", "jamaica", "ladder", "CLC"]
favourite_characters = ["^", ">", "<", "~"]

chosen_word = random.choice(favourite_words)
chosen_char = random.choice(favourite_characters)

chosen_num = random.randint(1, 100)

new_password = chosen_word + str(chosen_num) + chosen_char
print(new_password)

# Bonus
# new_password = [chosen_word, str(chosen_num), chosen_char]
# random.shuffle(new_password)
# new_password = "".join(new_password)
# print(new_password)
