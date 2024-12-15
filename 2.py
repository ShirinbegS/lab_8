def log(f):
    def d(x,y):
        r = f(x, y)
        print(f"log: {f.__name__}({x}+{y}) = {r}")
        return r
    return d
def add(x, y): return x + y

f = log(add)
print(f(1, 2))
print(f(3, 4))
print(f(128, 256))