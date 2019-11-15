# Put your name here
"""A simple script to test default parameters"""

def create_list(size = 10):
    """create a list of numbers from user input

    size:   an integer of how many numbers to read,
            defaults to 10"""

    print(size, "items to be asked for")
    
    numbers = list()
    for x in range(0, size):
        number = int(input("Please enter a number : "))
        numbers.append(number)

    return numbers

def main():
    """the function to kick it all off"""

    # Ask for 5 numbers
    numbers = create_list(5)
    print(len(numbers), "items:", numbers)

    # Use the default
    numbers = create_list()
    print(len(numbers), "items:", numbers)

if __name__ == '__main__':
    main()
        
