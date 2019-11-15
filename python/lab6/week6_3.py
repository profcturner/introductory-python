size = 10

words = []

for i in range(0, size):
    user_input = input("Enter word {} ".format(i))
    words.append(user_input)

for i in range(0, size):
    print("{}: {}".format(i, words[i]))
    
