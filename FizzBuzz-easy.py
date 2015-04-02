# FizzBuzz

def main():

    n = int(input('Enter a number: '))

    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print('Your number is not divisasble by 3, 5, or 15')

main()
