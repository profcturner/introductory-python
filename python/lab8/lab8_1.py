

def fetch_number(text='Enter a number: '):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print('That was not an integer.');

def main():
    numerator = fetch_number()
    denominator = fetch_number()

    try:
        division = numerator / denominator
    except ZeroDivisionError:
        print('Oops, division by zero...')
        division = 'undefined'

    print('Thanks, {} / {} is {}'.format(numerator, denominator, division))


if __name__ == '__main__':
    main()
