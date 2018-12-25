def triangles(max):
    n, l = 0, [1]
    while n < max:
        yield l
        l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
        l.insert(0, 1)
        l.insert(len(l), 1)
        n += 1
    return 'done'
if __name__ == '__main__':
    for l in triangles(20):
        print(l)
