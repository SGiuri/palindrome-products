def largest(min_factor, max_factor):

    first_factor = max_factor
    second_factor = max_factor
    value = first_factor * second_factor

    found = False
    factors = []

    for first_factor in range(max_factor,min_factor-1,-1):
        for second_factor in range(max_factor, min_factor - 1, -1):
            value = first_factor * second_factor
            if is_palindrome(value):
                found == True
                break
        if found:
            break
    print(value)



    pass


def smallest(min_factor, max_factor):
    pass


def is_palindrome(number):
    string_number = str(number)

    return string_number == string_number[::-1]

def find_factors(value, min_factor, max_factor):
    pass

largest(100,999)
