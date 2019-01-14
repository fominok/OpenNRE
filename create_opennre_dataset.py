
"""
The original KBP37 dataset has a structure like in those 2 examples:
    15917   " The <e1> Mississippi </e1> Air National Guard ( <e2> MS ANG </e2> ) is the air force militia of the State of Mississippi United States of America . "
    org:alternate_names(e2,e1)


    15918   " When the Gauche was excluded from the SFIO he became one of the leaders of the new Parti Socialiste Ouvrier et Paysan ( <e1> PSOP </e1> - Workers and Peasants <e2> Socialist Party </e2> ) and was at that time quite close to Leon Trotsky . "
    org:alternate_names(e2,e1)

--> we want to bring it into the JSON file format of OpenNRE!

"""


import json, sys, re, hashlib
from pprint import pprint

f = open(sys.argv[1]).readlines()

blocks = []
buf = []
for line in f:
    if line == '\n':
        blocks.append(buf.copy())
        buf = []
    else:
        buf.append(line.strip())

print(len(blocks))

examples = []
all_rels = set()

for block in blocks:
    rel_index = 0
    rel_line = None
    for i, line in enumerate(block):
        if line.find('(e1,e2)') > 0 or line.find('(e2,e1)') > 0 or line == 'Other':
            # Save relation index; data above is sentence, below -- comments
            rel_index = i
            rel_line = line
            break

    assert(rel_index != 0), 'No relation data for block {}'.format(block)

    main = re.search(r'"(.+)"$', ''.join(block[:rel_index]))[1] # Getting the sentence

    e1 = re.search('<e1>(.*)</e1>', main).group(1).strip()
    e2 = re.search('<e2>(.*)</e2>', main).group(1).strip()
    cl = main.replace('<e1>', '').replace('<e2>', '').replace('</e1>', '').replace('</e2>', '')
    print(cl, e1, e2)

    if rel_line.find('e1,e2') > 0:
        rel_type = rel_line.split('(')[0]
        print('rel_type', rel_type)

    elif rel_line.find('e2,e1') > 0:
        rel_type = rel_line.split('(')[0]
        e1, e2 = e2, e1

    elif rel_line == 'Other':
        rel_type = 'NA'

    else:
        raise Exception('Cannot parse relation: {}'.format(block))

    # else line == 'no_relation':
    #     rel_type = 'no_relation' 

    #elif len(line.strip()) == 0:
        ## add new example
        
    if e1:
        all_rels.add(rel_type)
        example = {'e1': e1, 'e2': e2, 'rel_type': rel_type, 'sentence': cl} 
        examples.append(example)
        e1 = ''

    else:
        raise Exception('What is this line: ***', block, '***')

print("Number of examples", len(examples))


def create_OpenNRE_dict(data):

        res = []

        for item in data:

            ## convert all relation types (except the NEGATIVE_TYPE) to BINARY_TYPE
            ## so for example "headquarter" --> 'locatedIn' .. 

            idh = hashlib.md5(item['e1'].encode('utf8')).hexdigest()
            idt = hashlib.md5(item['e2'].encode('utf8')).hexdigest()

            new_entry = { 'head': {'type':'UNK',  'word':item['e1'],  'id': idh},
                          'tail': {'type':'UNK',  'word':item['e2'],  'id': idt},
                          'relation': item['rel_type'],
                          'sentence': item['sentence']}

            print(new_entry)
            res.append(new_entry)

        print('Number of items in dataset:', len(res))
        return res


json_data = create_OpenNRE_dict(examples)
print(all_rels)
print(len(all_rels))

## create rel2id
rel2id = {'NA': 0}
all_rels_set = set(all_rels)
all_rels_set.remove('NA')
i = 1
for rel_type in all_rels_set:
    rel2id[rel_type] = i
    i = i + 1

print(rel2id)


with open('train.json', 'w') as outfile:
    json.dump(json_data, outfile)

with open('rel2id.json', 'w') as outfile:
    json.dump(rel2id, outfile)

print(len(examples))


