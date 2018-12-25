def num_to_str(n):
    while n>0:
        yield str(n % 10)
        n = int(n/10)

# def is_palindrom(n):
#     str_list = list(num_to_str(n))
#     l = len(str_list)

#     for i in range(0, int(l / 2)):
#         if str_list[i] != str_list[l - 1 - i]:
#             return False

#     return True

def is_palindrom(n):
    return str(n) == str(n)[::-1]
if __name__ == '__main__':
    print(list(filter(is_palindrom, range(1, 200))))
