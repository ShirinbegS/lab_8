def line(fn):
    f = open(fn, 'r')
    return  lambda: f.readline()
f = line('1.py')
print(f())
print(f())
print(f())
