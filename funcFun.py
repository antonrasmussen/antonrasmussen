


def get_numb(n):
    # Gets a number and returns that number.
    return n

def numb_plus_numb(n_plus):
    # Gets a number and returns that number plus itself.
    n_plus = int(n_plus)
    plus_numb = n_plus + n_plus
    return plus_numb
    



def main():
    print("")
    numb  = get_numb(input('Please enter a number: '))
    print("")
    print('Your result is: ', numb_plus_numb(numb))


main()
