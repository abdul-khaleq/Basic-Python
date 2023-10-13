# Python program to menostrate overriding in multiple inheritance 

# defining parent class 1 
class Parent1():
    # parent's show method
    def show(self):
        print('inside parent 1')

# defining parent class 2 
class Parent2:
    # parent's show method 
    def display(self):
        print('inside parent 2')

# defining child class 
class Child(Parent1, Parent2):
    # child's show method 
    def show(self):
        print('inside child')

# driver's code 
obj = Child()
obj.show()
obj.display()

# Python program to demonstrate overriding in multilevel inheritance 


# Python program to demonstrate overriding in multilevel inheritance 


class Parent(): 
		
	# Parent's show method 
	def display(self): 
		print("Inside Parent") 
	
	
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
		
	# Child's show method 
	def show(self): 
		print("Inside Child") 
	
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
		
	# Child's show method 
	def show(self): 
		print("Inside GrandChild")		 
	
# Driver code 
g = GrandChild() 
g.show() 
g.display() 
