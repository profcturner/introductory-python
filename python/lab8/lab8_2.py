# Writing a file
# Put your name here

def pick_filename():
    filename = input("Pick a filename: ")
    return filename

def read_file(filename):
    print("Attempting to open file {}".format(filename))
    with open(filename, 'r') as f:
        num_words = 0
        all_lines = f.read()
        lines = all_lines.splitlines()
        print("{} lines read.".format(len(lines)))
        for line in all_lines.splitlines():
            print(line)
            words = line.split()
            num_words += len(words)
        print("{} words in total.".format(num_words))
            
def main():
    filename = pick_filename()
    read_file(filename)

if __name__ == '__main__':
    main()
