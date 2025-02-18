#import pytest
def task1():
#Makes sure that hello world is printed
    x="Hello World!"
    value=0
    if x == "Hello World!":
        print(x)
        value = 1
    
    else:
        print("oh no")
    return value

def test_task1():
    assert task1() == 1

#task1()
test_task1()