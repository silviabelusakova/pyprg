# vyp min, max, vyfiltrovat kladne a zaporne cisla osobitne

import csv
import sys 
import statistics

file_name = sys.argv[1]

data = []

with open(file_name, 'r') as f:
    
    reader = csv.reader(f)
    
    for row in reader:

        for e in row:
            data.append(int(e))
    _min = min(data)
    _max = max(data)
    _len = len(data)
    _mean = statistics.mean(data)
    _median = statistics.median(data)

    print(f'mimimum is: {_min}')
    print(f'maximum is: {_max}')
    print(f'size is: {_len}')
    print(f'mean is: {_mean}')
    print(f'median is: {_median}')

    negative = [e for e in data if e < 0]
    positive = [e for e in data if e > 0]
   
    print(positive)
    print(negative)

