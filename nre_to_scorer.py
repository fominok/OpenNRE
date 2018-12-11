import json

with open('data/semeval/rel2id.json') as f:
    rels = json.load(f)

rels_rev = {v: k for k, v in rels.items()}

with open('test_result/semeval_pcnn_att_pred.json') as f:
    test_results = json.load(f)

with open('data/semeval/test.json') as f:
    test_data = json.load(f)

answers = {}
for i, t in enumerate(test_data):
    sent = t['sentence']
    e1_index = sent.find('e1')
    e2_index = sent.find('e2')
    assert e1_index and e2_index
    order_direct = e1_index < e2_index
    entpair_1 = t['head' if order_direct else 'tail']['id']
    entpair_2 = t['tail' if order_direct else 'head']['id']
    h = {
        'order_direct': order_direct,
        'relation_text': t['relation'],
        'relation_id': rels[t['relation']],
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

with open('answer_keys.txt', 'w') as f:
    for _, a in answers.items():
        rel_text = a['relation_text']
        if rel_text == 'NA':
            rel = 'Other'
        else:
            rel = rel_text + '(e1,e2)' if a['order_direct'] else '(e2,e1)'
        f.write(str(a['index']) + '\t' + rel + '\n')

with open('proposed_anwsers.txt', 'w') as f:
    for entpair, p in test_results_best.items():
        a = answers[entpair]
        order_direct = a['order_direct']
        rel = rels_rev[p['relation']] + '(e1,e2)' if order_direct else '(e2,e1)'
        index = a['index']
        f.write(str(index) + '\t' + rel + '\n')
