def greet(name):
    print(f'Hello {name}')

greet('Jim')


def check_even(number):
    if number%2==0:
        return (True)
    else:
        return (False)

is_even=check_even(13)
print(f'Is 13 even:{is_even}')

