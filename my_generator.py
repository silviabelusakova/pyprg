#!/urs/bin/env python

def countdown(num):

    print('Starting')

    while num > 0:
        yield num
        num -=1

for val in countdown(100):
    print(val)