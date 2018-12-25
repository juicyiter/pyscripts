def normalize(name):
    def conv(s):
        s = s.replace(s[0], s[0].upper())
        return s
    def norm(s):
        s = s.lower()
        return s
    return list(map(conv, list(map(norm, name))))

if __name__ == '__main__':
    print(normalize(['HELLO', 'world']))
