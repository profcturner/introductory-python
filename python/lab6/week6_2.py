size = 10

words = []

for i in range(0, size):
    user_input = input("Enter word %d " % i)
    words.append(user_input)

for i in range(0, size):
    print("%d: %s" % (i, words[i]))
    
