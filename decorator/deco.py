def deco(func):
    
    def inner(*args,**kwargs):
        print("hi")
        func(*args,**kwargs)
        print("bye")

    return inner



@deco
def sample(name,age):
    print("name :",name,"your age is:",age)
    print("good morning")

sample("joe",20)