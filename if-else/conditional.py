import random

def is_positive(num):
    if num>0:
        return True
    else:
        return False
    # return true if num is positive, otherwise return false

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    # return true if num is even, otherwise return false

def is_positive_and_even(num):
    if num>0 and num%2==0:
        return True
    else:
        return False
    # return true if num is positive and even, otherwise return false

def is_positive_or_even(num):
    if num>0 or num%2==0:
        return True
    else:
        return False
    # return true if num is positive or even, otherwise return false
num=random.randint(-10,10)
print(is_positive(num))
print(is_even(num))
print(is_positive_and_even(num))
print(is_positive_or_even(num))

