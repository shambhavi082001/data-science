import random

def generate_name():
    list1 = ['red', 'green', 'blue', 'yellow', 'orane',]
    list2 = ['apple', 'banana', 'mango', 'grape', 'pear']
    list3 = ['cat', 'dog', 'bird', 'fish', 'lion', 'tiger']

    p1 = random.choice(list1)
    p2 = random.choice(list2)
    p3 = random.choice(list3)
    
    return f'{p1}-{p2}-{p3}'