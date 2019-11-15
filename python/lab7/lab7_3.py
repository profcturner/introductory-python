import pickle

def pick_filename():
    filename = input("Pick a filename: ")
    return filename

def create_list():
    finished = False
    items = []
    while not finished:
        item = input("(text, empty to quit) ")
        if item != "":
            items.append(item)
        else:
            finished = True

    return items

def write_file(filename, items):
    print("Attempting to open file {}".format(filename))
    with open(filename, 'bw') as f:
        pickle.dump(items, f)

def read_file(filename):
    print("Attempting to open file {}".format(filename))
    with open(filename, 'rb') as f:
        items = pickle.load(f)
        return items

            
def main():
    filename = pick_filename()
    # Create a list
    items = create_list()
    # Save it to a file
    write_file(filename, items)
    # Load it from a file
    loaded_items = read_file(filename)
    # Print them
    print(loaded_items)
    # Check them
    if items == loaded_items:
        print("restored correctly")

if __name__ == '__main__':
    main()
        
