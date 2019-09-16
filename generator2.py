def countdown():

    num = 0 
    print('Starting')

    while True:
        yield num
        num -=1

max_iter = 1000
i = 0

for val in countdown():
    print(val)
    i +=1
    if i >= max_iter:
        break 

# with open('data.txt', 'r') as f:

#     for line in f:
#         print(line)