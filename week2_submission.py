import numpy as np

def first_n_fibonacci(n):
    # Use Binet's formula for fibonacci numbers in a list comprehension
    return [
        int(np.fix( 
            ( ((1+np.sqrt(5)) / 2)**i - ((1-np.sqrt(5)) / 2)**i )/np.sqrt(5) 
        ))
        for i in range(n)
    ]\

# print(first_n_fibonacci(10))