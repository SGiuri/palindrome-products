def largest(min_factor, max_factor):

    first_factor = max_factor
    second_factor = max_factor
    value = first_factor * second_factor

    max_value = max_factor*max_factor
    min_value = min_factor*min_factor
    palindrome = []
    for first_factor in range(max_factor, min_factor, -1):
        for second_factor in range(max_factor, first_factor, -1):
            value = first_factor * second_factor
            if is_palindrome(value) and value not in palindrome:
                palindrome.append(value)
    max_value  = max(palindrome)
    factors = find_factors(max_value, min_factor, max_factor)

    return max_value,

    pass


def smallest(min_factor, max_factor):
    pass


def is_palindrome(number):
    string_number = str(number)

    return string_number == string_number[::-1]


def find_factors(value, min_factor, max_factor):
    factors = []
    for j in range(min_factor, max_factor):
        if value % j == 0:
            print(value, j, value//j)
            if min_factor < (value // j) < max_factor:
                factors.append([j, value // j])
    return factors


largest(100, 999)

print(find_factors(580085, 100, 999))
