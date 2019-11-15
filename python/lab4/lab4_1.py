# Import os so this will work on any operating system
import os

print('Some information\n')

print('Operating System Shortname', os.name)
print('Details')
print(os.uname())


finished = False
while not finished:
    # Prompt the user for a pathname
    pathname = input('Give a directory to list: ')
    # If it's empty, default to the current dir
    # and flag that we will quit after this loop
    if(pathname == ''):
        pathname = '.'
        finished = True
        
    files = os.listdir(pathname)
    for file in files:
        print('\t', file)




