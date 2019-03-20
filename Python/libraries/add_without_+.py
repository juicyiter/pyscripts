def add_two_num(a, b):
    # write your code here
    if a | b < 0 and abs(a) == abs(b):
        return 0
    res = 0
    hold = 0
    i = 0
    flag = 0
    while a not in [-1, 0] or b not in [-1, 0]:
        b_a = a & 1
        b_b = b & 1
        t = b_a ^ b_b ^ hold
        res |= (t << i)
        i += 1
        if b_a ^ b_b == 0:
            hold = b_a

        a = a >> 1
        b = b >> 1

    res |= (hold << i)
    res = (a << i) | res | (b << i)
    return res

def add(a, b):
    
print(add_two_num(-1, 1))
