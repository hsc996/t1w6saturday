# count vowels and consonant in a string
# count the number of capital / upper case letters
# removes spaces from string without string methods

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

num_vowels = 0

for character in sentence:
    if character.lower() in 'aeiou':
        num_vowels += 1

print(f"Number of vowels: {num_vowels}")
