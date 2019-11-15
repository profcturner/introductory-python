# Learning about if
# Place your name here

# Get a string from the user
user_input = input("Please enter an integer: ")
if not user_input.isnumeric():
    print("that wasn't an integer you know...")
else:
    print("thanks")
    # Ok, let's put this into a float variable
    number1 = int(user_input)
    
# Get a string from the user
user_input = input("Please enter another integer: ")
if not user_input.isnumeric():
    print("that wasn't an integer you know...")
else:
    print("thanks")
    # Ok, let's put this into a float variable
    number2 = int(user_input)

# Let's compare these
if number1 > number2:
    print("Hmm. the first number was bigger")
elif number2 > number1:
    print("the second number was bigger")
else:
    print("ah, nice try, they were the same")


    

