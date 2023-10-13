# Function is a first class object

def double_decker():
    print('Starting the double decker')
    def inner_func():
        print('Inside the inner')
        return 'Inside done'
    return inner_func

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ended')
def conding():
    print('coding in Python')

# do_something(conding)

def sleeping():
    print('sleeping and dreaming in Python')

do_something(sleeping)
