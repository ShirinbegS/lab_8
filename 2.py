def log(f):
    def d(x,y):
        print(f"log: {f.__name__}({x}+{y}) = {f(x,y)}")
        return f(x,y)
    return d
@log
def add(x, y): 
    return x + y

print(add(1, 2))
print(add(3, 4))
print(add(128, 256))