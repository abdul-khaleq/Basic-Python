# Python program illustrate how to overload an binary + operator and how it actually works 
class A:
    def __init__(self, a) -> None:
        self.a = A
    
    # adding two objects 
    def __add__(self, o):
        return self.a + o.a

ob1 = A(1)