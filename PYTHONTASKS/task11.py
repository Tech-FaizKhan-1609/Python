def number_generator():
    for i in range(1, 101):
        yield i

generator = number_generator()

for number in generator:
    print(number)