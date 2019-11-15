# Learning about while and lists too
# Put your name here

# Create an empty list
words = list()
finished = False

# Let's do this repeatedly
while not finished:
    word = input("Give me a word or two, (empty to quit) : ")
    if word == "":
        # The word was empty
        finished = True
    else:
        words.append(word);


# Can we print it out again?
print("Ok, so that was", len(words), "entries and they were")

# Loop again, in another way
for x in words:
    print(x)
