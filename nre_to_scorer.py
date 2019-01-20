import json
import sys

# Load OpenNRE dataset with test results

if len(sys.argv) > 1:
    dataset_name = sys.argv[1]

with open(f'data/{dataset_name}/rel2id.json') as f:
    rels = json.load(f)

rels_rev = {v: k for k, v in rels.items()}

with open(f'test_result/{dataset_name}_pcnn_att_pred.json') as f:
    test_results = json.load(f)

with open(f'data/{dataset_name}/test.json') as f:
    test_data = json.load(f)

answers = {}
for i, t in enumerate(test_data):
    sent = t['sentence']
    # Find positions of words in dataset record
    e1_index = sent.find(t['head']['word'])
    e2_index = sent.find(t['tail']['word'])
    # Ensure that both related words are found
    assert e1_index is not None and e2_index is not None

    # For SemEval order of related words is stored in (e2,e1) or (e1,e2) format
    # Using indexes of words we can restore this information
    order_direct = e1_index < e2_index
    entpair_1 = t['head']['id']
    entpair_2 = t['tail']['id']
    h = {
        'order_direct': order_direct,
        'relation_text': t['relation'],
        'relation_id': rels[t['relation']],
        # Entpair is a concat of word ids from dataset used in test results
        'entpair': entpair_1 + '#' + entpair_2,
        'index': i + 1,
    }
    answers[h['entpair']] = h

test_results_best = {}
for tr in test_results:
    e = tr['entpair']
    if test_results_best.get(e) is None:
        test_results_best[e] = tr
    else:
        tr_old = test_results_best[e]
        if tr_old['score'] < tr['score']:
            test_results_best[e] = tr

# Convert answers from OpenNRE test data format to SemEval scorer
with open('answer_keys.txt', 'w') as f:
    for _, a in answers.items():
        rel_text = a['relation_text']
        if rel_text == 'NA':
            rel = 'Other'
        else:
            rel = rel_text + ('(e1,e2)' if a['order_direct'] else '(e2,e1)')
        f.write(str(a['index']) + '\t' + rel + '\n')

# Convert proposed answers from OpenNRE format with entpairs to SemEval scorer
with open('proposed_anwsers.txt', 'w') as f:
    for entpair, p in test_results_best.items():
        a = answers[entpair]
        order_direct = a['order_direct']
        rel = rels_rev[p['relation']] + \
            ('(e1,e2)' if order_direct else '(e2,e1)')
        index = a['index']
        f.write(str(index) + '\t' + rel + '\n')
