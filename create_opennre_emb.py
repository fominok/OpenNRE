import json
import sys

"""
    convert word embedding vector (text) format into OpenNRE json format
    
    OpenNRE json looks like this:
    [
        {'word': 'the', 'vec': [0.418, 0.24968, ...]},
        {'word': ',', 'vec': [0.013441, 0.23682, ...]},
        ...
    ]
"""

results = []

with open(sys.argv[1], 'r') as f:
    next(f)
    for line in f:

        ele = line.strip().split(' ')
        word = ele[0]
        vec = [float(e) for e in ele[1:]]
        assert len(vec) == len(ele) - 1

        results.append( {'word': word, 'vec': vec} )

json.dump(results, open('new.json', 'w'))

