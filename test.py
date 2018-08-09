secret_word = 'apple'
lettres_guessed = ['e', 'i', 'k', 'p', 'r', 's']
i = 0
underscores = (len(secret_word)*"_ ")
for letter in secret_word:
    if letter in secret_word:
        underscores.replace((underscores[i]),(secret_word[i]))
        i += 1
    else:
        i += 1
print(underscores)


output = ""

