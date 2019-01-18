import json
import os
import sys
import spacy


def replace_coreferences(raw_text):
    print("replacing coreferences...")
    nlp = spacy.load('en_coref_md')

    for index, item in enumerate(raw_text):
        print("processing entry {0}... \r".format(str(index + 1)), end='', flush=True)
        doc = nlp(item["abstract"])
        coref_text = doc._.coref_resolved
        if len(coref_text) > 0:
            item["abstract"] = coref_text

    return raw_text


if __name__ == '__main__':
    print("Reading raw data...")

    raw = json.load(open('./data/raw.json'))

    print("done; replacing coreferences...")

    count = 1000
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    replaced = replace_coreferences(raw[:count])

    target_path = "./data"
    target_file = "raw-with-replaced-coreferences.json"
    print("done; writing to {0}/{1} file...".format(target_path, target_file))

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    json.dump(replaced, open("{0}/{1}".format(target_path, target_file), "w+"))

    print("done; ready to annotate")
