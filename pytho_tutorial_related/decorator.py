import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        f = fn(*args, **kw)
        end = time.time()
        print('%s executed %s ms' % (fn.__name__, end-start))
        return f
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)

print(f)
print(s)
