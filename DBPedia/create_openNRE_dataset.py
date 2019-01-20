# -*- coding: utf-8 -*-
import sys

sys.path.append('..')

import json, hashlib, sys, nltk
import re
from dateutil import parser


# Configuration section
TRAIN_FILE = "data/train.json"
TEST_FILE = "data/test.json"
EMB_FILE = 'data/word_vec.json'

SENTENCE_MUST_CONTAIN_COMPANY = True        # only include sentences in the result that contain the company_name
BINARY_RELATION = True
SKIP_IF_NOT_FOUND_IN_EMBEDDINGS = True
FIRST_SENTENCE_ONLY = True
REPLACE_COMPANY_NAME = True                 # convert sentences to lowercase (needed for OpenNRE)
COMPANY_NAME_REPLACEMENT = "IBM"            # convert sentences to lowercase (needed for OpenNRE)

NEGATIVE_TYPE = 'Unrelated'
BINARY_TYPE = 'locatedAt'
year_pattern = re.compile('[0-9]{3,4}')     # naive version, takes just 3 or for digit numbers


# class for representing information about company
class CompanyRelation:
    def __init__(self, company_name, sentence, date, relation_type):

        self.company_name = company_name
        self.foundation_date = date
        self.relation_type = relation_type

        if type(sentence) == type([]):
            self.sentence = ' '.join(sentence)
        else:
            self.sentence = sentence

        if len(date.split(' ')) > 1:
            self.foundation_date = date.replace(' ', '_')

            # also replace in sentence
            self.sentence = self.sentence.replace(date, self.foundation_date)

        # replace " " with "_" in company_name and sentence
        if len(company_name.split(' ')) > 1:
            self.company_name = company_name.replace(' ', '_')

            # also replace in sentence
            self.sentence = self.sentence.replace(company_name, self.company_name)

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
            return True
        else:
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
    dates = year_pattern.findall(sent)          # TODO: search not only year

    return dates


def create_dataset(companies_data):
    ds_items = []

    for company_data in companies_data:
        foundation_date = parser.parse(company_data['year'])
        sentences = nltk.sent_tokenize(company_data["abstract"])
        company_name = company_data['company'];
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

        for sent_id, sentence in enumerate(sentences):
            dates = extract_naive_dates(sentence)
            tokenized_sentence = tokenized_sentences[sent_id]

            make_positive_relations(company_name, foundation_date, dates, tokenized_sentence, ds_items)
            make_negative_relations(company_name, foundation_date, dates, tokenized_sentence, ds_items)

    return companies_data, ds_items


def make_negative_relations(company_name, foundation_date, dates, tokenized_sentence, ds_items):
    for date in dates:
        if str(foundation_date.year) == date:
            continue
        else:
            item = CompanyRelation(company_name, tokenized_sentence, date, NEGATIVE_TYPE)
            ds_items.append(item)


def make_positive_relations(company_name, foundation_date, dates, tokenized_sentence, ds_items):
    if str(foundation_date.year) in dates:
        date_str = str(foundation_date.year)
        item = CompanyRelation(company_name, tokenized_sentence, date_str, BINARY_TYPE)
        ds_items.append(item)


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

        res.append(new_entry)

    print('Number of items in dataset:', len(res))
    return res


def write_dl_dataset(ds_items):
    """ finally, write everything to the target file
    """

    split = int(len(ds_items) * 0.8)
    train_ds = ds_items[:split]
    test_ds = ds_items[split:]

    train_opennre = create_OpenNRE_dict(train_ds)
    test_opennre = create_OpenNRE_dict(test_ds)

    with open(TRAIN_FILE, 'w', encoding='utf8') as outfile:
        json.dump(train_opennre, outfile)

    with open(TEST_FILE, 'w', encoding='utf8') as outfile:
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
    count = None
    if len(sys.argv) > 1:
        count = int(sys.argv[1])

    print('creating dataset started\n')
    data = json.load(open('./data/raw-with-replaced-coreferences.json'))

    if count:
        data = data[:count]

    data, ds_items = create_dataset(data)
    ds_items = filter_ds_items(ds_items, sentence_must_contain_company=SENTENCE_MUST_CONTAIN_COMPANY)
    ds_items = check_if_NEs_in_embeddings(ds_items, EMB_FILE)
    write_dl_dataset(ds_items)
