def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    def __init__(self):
        print("MyClass initialized")


# Usage
x = MyClass()
y = MyClass()

print(x is y)  # True
