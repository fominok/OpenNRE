import json
import sys
import re
import hashlib
from pprint import pprint

# Reading SemEval dataset contents

f = open(sys.argv[1]).readlines()

blocks = []
buf = []
for line in f:
    if line == '\n':
        blocks.append(buf.copy())
        buf = []
    else:
        buf.append(line.strip())

f.close()

print(len(blocks))

examples = []
all_rels = set()

# Each block represents a dataset record
for block in blocks:
    # rel_index stands for a number of line where relation info located in
    # Usually it is a second line but it's not guaranteed
    rel_index = 0
    rel_line = None
    for i, line in enumerate(block):
        if line.find('(e1,e2)') > 0 or line.find('(e2,e1)') > 0 or line == 'Other':
            rel_index = i
            rel_line = line
            break

    # If no line in a record contains relation info (any relation or Other)
    # dataset is probably broken
    assert(rel_index != 0), 'No relation data for block {}'.format(block)

    # Getting the sentence
    # We use block[:rel_index] here because sentense is all text before relation line
    main = re.search(r'"(.+)"$', ''.join(block[:rel_index]))[1]

    # Find words with relation information provided
    e1 = re.search('<e1>(.*)</e1>', main).group(1).strip()
    e2 = re.search('<e2>(.*)</e2>', main).group(1).strip()

    # Cleanup sentence from tags as OpenNRE dataset uses clean sentences without tag embeddings
    cl = main.replace('<e1>', '').replace(
        '<e2>', '').replace('</e1>', '').replace('</e2>', '')
    print(cl, e1, e2)

    # Relation type is written right before parens
    if rel_line.find('e1,e2') > 0:
        rel_type = rel_line.split('(')[0]
        print('rel_type', rel_type)
    # Related words may be placed in reverse order
    elif rel_line.find('e2,e1') > 0:
        rel_type = rel_line.split('(')[0]
        # So we have to swap them
        e1, e2 = e2, e1
    elif rel_line == 'Other':
        rel_type = 'NA'
    else:
        raise Exception('Cannot parse relation: {}'.format(block))

    assert(e1 and e2 and rel_type), 'Error parsing relation data: {}'.format(block)
    all_rels.add(rel_type)
    example = {'e1': e1, 'e2': e2, 'rel_type': rel_type, 'sentence': cl}
    examples.append(example)

print("Number of examples", len(examples))


def create_open_nre_dict(data):
    res = []
    for item in data:
        # Every words requires its own id, same words have same ids
        idh = hashlib.md5(item['e1'].encode('utf8')).hexdigest()
        idt = hashlib.md5(item['e2'].encode('utf8')).hexdigest()

        # Create a dataset record in a proper OpenNRE format
        new_entry = {'head': {'type': 'UNK',  'word': item['e1'],  'id': idh},
                     'tail': {'type': 'UNK',  'word': item['e2'],  'id': idt},
                     'relation': item['rel_type'],
                     'sentence': item['sentence']}
        print(new_entry)
        res.append(new_entry)
    return res


json_data = create_open_nre_dict(examples)
print(all_rels)
print(len(all_rels))

# create rel2id
rel2id = {'NA': 0}
all_rels.remove('NA')
i = 1
for rel_type in all_rels:
    rel2id[rel_type] = i
    i = i + 1

print(rel2id)

# Write dataset into json file
with open('train.json', 'w') as outfile:
    json.dump(json_data, outfile)

with open('rel2id.json', 'w') as outfile:
    json.dump(rel2id, outfile)

print(len(examples))
