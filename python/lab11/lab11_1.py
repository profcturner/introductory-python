# Random numbers

import random

def guess_my_number(lowest=1, highest=100):
    # Generate the number
    number = random.randrange(lowest, highest+1)

    guessed = False
    while not guessed:
        guess = int(input("What number am I thinking of? "))

        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        else:
            print("Correct!")
            guessed = True


def rock_paper_scissors():
    choices = ['rock','paper','scissors']

    print("Pick one of the following")
    index = 1
    for choice in choices:
        print("{}. {}".format(index, choice))
        index += 1

    number = int(input("Pick 1, 2 or 3: "))
    # Python uses 0 for the first item in a list, subtract 1
    user_choice = choices[number-1]
    print("You picked {}".format(user_choice))

    # Ok, now the computer choice, we can use a function
    # random.choice() to pick one item at random from a list
    computer_choice = random.choice(choices)
    print("I picked {}".format(computer_choice))
          

    



def main():
    rock_paper_scissors()
    guess_my_number()

if __name__ == '__main__':
    main()
