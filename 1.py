def read_file(fn):
    file = open(fn, 'r')
    def next_line():
        line = file.readline()
        if line:
            return line.strip()
    return next_line

f = read_file('1.py')
print(f())
print(f())