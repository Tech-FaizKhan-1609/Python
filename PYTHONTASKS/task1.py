class MyClass:
    def __init__(self,variable):
        self.variable=variable
class OtherClass:
        def __init__(self,local):
             self.local=local
obj=MyClass("Hello,instance variable")
vae=OtherClass("bye")
instance=obj.variable
li=vae.local
print(li)
print(instance)             