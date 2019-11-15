class Person(object):
    ''' Describes a person

    name    the name of the person
    age     the age of the person
    '''
    def __init__(self):
        self.name = ''
        self.email = ''
        self.age = 0

    def __str__(self):
        return self.name + ' email: ' + str(self.email) + ' age: ' + str(self.age)

    def input(self):
        self.name = input('Enter a name :')
        self.email = input('Enter an email address :')
        self.age = int(input('Enter the age :'))



def main():
    joe = Person()

    print(joe.name)
    print(joe.age)

    joe.input()

    print(joe.name)
    print(joe.age)
    print(joe)

if __name__ == '__main__':
    main()
    
