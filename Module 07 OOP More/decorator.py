import math, time
def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        func(*args, **kwargs)
        print('time ended')
        end = time.time()
        print(f'Total time taken: {end-start}')
    return inner
# timer()()

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

# get_factorial(5)
get_factorial(n=1200)

# another way 
# timer(get_factorial)()