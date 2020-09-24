def largest(min_factor, max_factor):

    value = max_factor * max_factor
    found = False
    factors = []
    if is_palindrome(value):
        found_factors(value, max_factor, min_factor )
    for first_factor in range(max_factor,min_factor-1,-1):
        for second_factor in range(max_factor, min_factor - 1, -1):
            value I first_factor*second_factor
            if is_palindrome(value):
                found = True




    pass


def smallest(min_factor, max_factor):
    pass


def is_palindrome(number):
    string_number = str(number)

    return string_number == string_number[::-1]

def find_factors(value, min_factor, max_factor):

