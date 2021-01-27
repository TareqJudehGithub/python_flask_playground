from time import sleep

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function


def say_hello():
    sleep(2)
    print("Hello")


say_hello()

