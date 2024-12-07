# Настройка логирования
def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        return result
    return wrapper

# Пример использования
def example_function(x, y):
    return x + y

# Тест вызова
if __name__ == "__main__":
    example_function(5, 10)

print(log_calls(1, 2))
print(f(3, 4))
print(f(128, 256))