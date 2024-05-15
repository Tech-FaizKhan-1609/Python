def table_of_5():
    num = 1
    while True:
        yield num * 5
        num += 1

generator = table_of_5()

for i in range(10): 
    print(next(generator))