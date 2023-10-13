class GrandFather:
    def __init__(self) -> None:
        pass
    def property(self):
        print("I have 3 core Taka")

class Father(GrandFather):
    def property(self):
        print("I have 2 core Taka")
    def father_property(self):
        super().property()

class Child(Father):
    def property(self):
        print("I have 1 core Taka")
    def father_property(self):
        super().property()
    def grand_father_property(self):
        super().father_property()

me = Child()
me.property()
me.father_property()
me.grand_father_property()