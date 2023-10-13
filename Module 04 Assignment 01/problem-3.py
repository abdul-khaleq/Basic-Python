# List and Dictinary is build in function these are used to store data in Python. A List is a collection of orderd data, on the other hand, A dictionary is a unorderd collection of data which save key value of pair.
# A list is mutable that can change value using index when needed while A dictonary is also mutable but its key is not duplicatable. Dictinary is changed using its key.
# Two examples are bellow how to use them

#create a list
nameOfStudents = ['Abdulah', 'Jibon', 'Mofig']
#create a dictionary
students = {'1': 'Abdullah', '2': 'Jibon'}

# *args allow to pass multiple arguments to a function. single asterisk * is used to pass as perameter to function. there can be used any names but *.


def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum = sum + n
    print(sum)
add(1,2,3,4,5)

# **kwargs allow to pass keyword arguments as parameters to function.duble asterisk ** is used to pass as parameter to function as keyword argument. **kwargs accept as dictionary of key value pair to function.
# Below is an example

def founder(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key ,' : ', value)
founder(name='Abdul Khaleq', age='25', cityName='Bogura')