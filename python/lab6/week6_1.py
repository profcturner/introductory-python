import re

def test_input(istring):
    re_start_hello = r'^hello'
    re_end_world = r'world$'

    if(re.fullmatch(re_start_hello, istring) != None):
        print("Start with hello")
 

def main():

    finished = False

    while not finished:
        test_string = input("Enter a string, empty to quit: ")
        if test_string == "":
            finished = True
        else:
            test_input(test_string)


if __name__ == '__main__':
    main()
  
