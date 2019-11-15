# Experiments with pdb
# Put your name here

def create_word_list(text=""):
    if len(text):
        print(text)

    words = []

    for x in range(0, 5):
        word = input("A word please: ")

    words.append(word)
    return words

def interleave_lists(list1, list2):
    final_list = []

    for x in range(0, 5):
        word1 = list1[x]
        word2 = list2[x]

        final_list.append(word1)
        final_list.append(word2)
        
    return final_list

def main():

    list1 = create_word_list("First list.")
    list2 = create_word_list("Second list.")

    final_list = interleave_lists(list1, list2)

    print(final_list)

if __name__ == '__main__':
    main()
