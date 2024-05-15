def new_func():
    class MyClass:
        def __init__(self, name):
            self.name = name
    
        def __del__(self):
            print(f"Destructor called for {self.name}")


    obj1 = MyClass("Object 1")
    obj2 = MyClass("Object 2")


    del obj1
    del obj2

new_func()
