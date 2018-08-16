import string
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
alphabet = string.ascii_lowercase
for letter in letters_guessed:
    alphabet = alphabet.replace(letter, "")

print(alphabet)
