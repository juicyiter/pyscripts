def power(x, y):
    # if y is times of 2, half and recursion
    # else half + 1 and recursion
    result = 1.0
    if y < 0:
        x, y = 1.0 / x, -y

    while y:
        if y & 1:
            result *= x
        x, y = x * x, y >> 1

    return result


power(2, 5)
