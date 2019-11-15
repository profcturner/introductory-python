def hello_world():
    """This is a really basic function that takes
    no arguments and returns no arguments"""
    print("Hello World")

def add_numbers(number1, number2):
    """This takes two numbers and adds them together
    and returns the result"""
    result = number1 + number2
    return(result)

def read_number():
    """Asks for a number and returns it"""
    number = int(input("Please enter a number : "))
    return(number)

def main():
    """The function that brings it all together"""
    hello_world()
    a = read_number()
    b = read_number()
    addition = add_numbers(a, b)

    print(a, "plus", b, "is", addition)

if __name__ == '__main__':
    main()
