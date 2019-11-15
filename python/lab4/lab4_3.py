# Some fun with the math module
# Put your name here
import math

# Let's look at angles from 0 to 720 every 15 degrees
angles = range(0,720,15)

# Look at each of these steps
for angle in angles:
    # Most trig functions need a thing called radians
    # Do the conversion
    radians = math.radians(angle)
    # Work out the sine of the angle
    sine = math.sin(radians)

    # This is a number from -1 to 1
    # Let's scale it from 10 to 50
    number_spaces = math.floor(20 * sine + 30)

    # Work out a gap by multiplying a string by
    # a number to make it that long, cool huh?
    spaces = ' ' * number_spaces
    # Print the gap, then an o
    print(spaces, 'o')
     
