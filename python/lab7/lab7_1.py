

def pick_filename():
    filename = input("Pick a filename: ")
    return filename

def write_file(filename):
    print("Attempting to open file {}".format(filename))
    finished = False
    with open(filename, 'w') as f:
        while not finished:
            line = input("(text, empty to quit) ")
            if line != "":
                #print(line, file=f)
                f.write(line + '\n')
            else:
                finished = True
            
def main():
    filename = pick_filename()
    write_file(filename)

if __name__ == '__main__':
    main()
        
