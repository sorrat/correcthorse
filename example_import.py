from correcthorse import generate_wordlist, generate_xkcdpassword

# create a wordlist
mywords = generate_wordlist(
    wordfile='correcthorse/3esl.txt',
    min_length=5,
    max_length=8,
)

# create a password with the acrostic 'face'
print generate_xkcdpassword(mywords, acrostic="face")
