# Learning about for and lists too
# Put your name here

# Control how big the list gets
size = 10

# Create an empty list
numbers = list()

# Let's do this repeatedly
for x in range(0, size):
    number = int(input("%u: Give me an integer :" % x))
    # Now let's add this to the list with this nifty append
    numbers.append(number)

# Can we print it out again?
print("Ok, so that was:")

# Loop again, in another way
for x in numbers:
    print(x)


