# -*- coding: utf-8 -*-
import sys

sys.path.append('..')

import json, hashlib, sys, nltk
import re
from dateutil import parser


############################### configuration section ##################################
TRAIN_FN = "data/train.json"
TEST_FN = "data/test.json"
SENTENCE_MUST_CONTAIN_COMPANY = True  ## only include sentences in the result that contain the company_name
BINARY_LOCATION = True
SKIP_IF_NOT_FOUND_IN_EMBEDDINGS = True
EMB_FILE = 'data/word_vec.json'
##FULL_PARAGRAPH=False# instead of sentences, use the full paragraph as input data?
FIRST_SENTENCE_ONLY = True
TO_LOWER = False  ## convert sentences to lowercase (needed for OpenNRE_old)
REPLACE_COMPANY_NAME = True  ## convert sentences to lowercase (needed for OpenNRE)
COMPANY_NAME_REPLACEMENT = "IBM"  ## convert sentences to lowercase (needed for OpenNRE)

#################### constants
NEGATIVE_TYPE = 'Unrelated'
BINARY_TYPE = 'locatedAt'
tag_pattern = re.compile('[0-9]{3,4}')

count = None
if len(sys.argv) > 1:
    count = int(sys.argv[1])


class DSItem:
    def __init__(self, sentence, company_name, date, relation_type):

        self.company_name = company_name
        self.foundation_date = date
        self.relation_type = relation_type

        if type(sentence) == type([]):
            self.sentence = ' '.join(sentence)
        else:
            self.sentence = sentence

        if len(date.split(' ')) > 1:
            self.foundation_date = date.replace(' ', '_')

            ## also replace in sentence
            self.sentence = self.sentence.replace(date, self.foundation_date)

        ##  replace " " with "_" in company_name and sentence
        if len(company_name.split(' ')) > 1:
            self.company_name = company_name.replace(' ', '_')

            ## also replace in sentence
            self.sentence = self.sentence.replace(company_name, self.company_name)

        if TO_LOWER:
            self.sentence = self.sentence.lower()
            self.company_name = self.company_name.lower()
            self.foundation_date = self.foundation_date.lower()

        if REPLACE_COMPANY_NAME:
            self.sentence = self.sentence.replace(self.company_name, COMPANY_NAME_REPLACEMENT)
            self.company_name = COMPANY_NAME_REPLACEMENT

    def print_me(self):
        print("\n DSItem")
        print("Company: ", self.company_name)
        print("Location: ", self.foundation_date)
        print("LocationType: ", self.relation_type)
        print("Sentence: ", self.sentence)

    def sentence_contains_company(self):

        if self.sentence.replace(' ', '').find(self.company_name.replace(' ', '')) > -1:
            # print('contains:', self.company_name, '//', self.sentence)
            return True
        else:
            # print('NOT contains:', self.company_name, '//', self.sentence)
            return False


def annotate(raw_entry):
    sentences = nltk.sent_tokenize(raw_entry["abstract"])
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

    annotated_text = []
    for tree in chunked_sentences:
        annotated_text.append(tree)

    raw_entry["abstract_annotated"] = annotated_text
    raw_entry["tokenized_sentences"] = tokenized_sentences
    raw_entry["tagged_sentences"] = tagged_sentences
    raw_entry["raw_sentences"] = sentences

    return raw_entry


def extract_naive_dates(sent):
    # tokens = nltk.word_tokenize(sent);
    dates = tag_pattern.findall(sent)

    return dates


def create_dataset(companies_data):
    ds_items = []
    for company_data in companies_data:
        foundation_date = parser.parse(company_data['year'])

        sentences = nltk.sent_tokenize(company_data["abstract"])
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        for sid, sentence in enumerate(sentences):
            # print(sentence)
            dates = extract_naive_dates(sentence)
            if str(foundation_date.year) in dates:
                date_str = str(foundation_date.year)
                # print('add positive relation ' + company_data['company'] + ' date = ' + date_str)
                # print('\n')
                item = DSItem(tokenized_sentences[sid], company_data['company'], date_str, BINARY_TYPE)
                ds_items.append(item)

            for date in dates:
                if str(foundation_date.year) == date:
                    # print(date + ' = ' + str(foundation_date.year))
                    # print('\n')
                    continue
                else:
                    # print('add negative relation for' + company_data['company'] + ' date = ' + date)
                    # print('\n')
                    item = DSItem(tokenized_sentences[sid], company_data['company'], date, NEGATIVE_TYPE)
                    ds_items.append(item)

    return companies_data, ds_items


def filter_ds_items(ds_items, sentence_must_contain_company=False):
    filtered_ds_items = []
    print("filter_sentence_must_contain_company: Number of items at entry:", len(ds_items))

    for ds_item in ds_items:

        if sentence_must_contain_company and not ds_item.sentence_contains_company():
            continue

        filtered_ds_items.append(ds_item)

    print("filter_sentence_must_contain_company: Number of items at exit:", len(filtered_ds_items))

    return filtered_ds_items


def create_OpenNRE_dict(data):
    res = []

    for item in data:
        idh = hashlib.md5(item.company_name.encode('utf8')).hexdigest()
        idt = hashlib.md5(item.foundation_date.encode('utf8')).hexdigest()
        new_entry = {
            'head': {'type': 'COMPANY', 'word': item.company_name, 'id': idh},
            'tail': {'type': 'FOUNDATION_DATE', 'word': item.foundation_date, 'id': idt},
            'relation': item.relation_type,
            'sentence': item.sentence
        }

        # print(new_entry)
        res.append(new_entry)

    print('Number of items in dataset:', len(res))
    return res


def write_dl_dataset(ds_items):
    """ finally, write everything to the target file
    """

    split = int(len(ds_items) * 0.8)
    train_ds = ds_items[:split]
    test_ds = ds_items[split:]

    # [ds_item.write(train_fh) for ds_item in train_ds]
    # [ds_item.write(test_fh)  for ds_item in test_ds]

    train_opennre = create_OpenNRE_dict(train_ds)
    test_opennre = create_OpenNRE_dict(test_ds)

    # train_fh = open(TRAIN_FN, 'w')
    # test_fh  = open(TEST_FN, 'w')

    with open(TRAIN_FN, 'w', encoding='utf8') as outfile:
        json.dump(train_opennre, outfile)

    with open(TEST_FN, 'w', encoding='utf8') as outfile:
        json.dump(test_opennre, outfile)


def check_if_NEs_in_embeddings(ds_items, emb_fn):
    data = json.load(open(emb_fn))
    words = [d['word'] for d in data]

    print('\nNumber of words in the embeddings:', len(words))

    company_found, company_not_found = 0, 0

    filtered_ds_items = []

    for d in ds_items:
        if d.company_name.lower() in words:
            company_found = company_found + 1
        else:
            company_not_found = company_not_found + 1

        if SKIP_IF_NOT_FOUND_IN_EMBEDDINGS:
            if d.company_name.lower() in words:
                filtered_ds_items.append(d)
        else:
            filtered_ds_items.append(d)

    print("check_if_NEs_in_embeddings: Number company_found", company_found)
    print("check_if_NEs_in_embeddings: Number company_not_found", company_not_found)

    return filtered_ds_items


if __name__ == '__main__':
    print('creating dataset started\n')
    data = json.load(open('./data/raw-with-replaced-coreferences.json'))

    if count:
        data = data[:count]

    data, ds_items = create_dataset(data)
    ds_items = filter_ds_items(ds_items, sentence_must_contain_company=SENTENCE_MUST_CONTAIN_COMPANY)
    ds_items = check_if_NEs_in_embeddings(ds_items, EMB_FILE)
    write_dl_dataset(ds_items)
