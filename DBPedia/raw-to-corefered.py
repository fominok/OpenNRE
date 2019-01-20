import json
import os
import sys
import spacy

# constants
ITEMS_COUNT = 1000
TARGET_PATH = "./data"
TARGET_FILE = "raw-with-replaced-coreferences.json"


# It should change all pronouns in abstract with company name. It allows to find relation between
# company name and foundation year
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


def main():
    print("Reading raw data...")

    raw = json.load(open('./data/raw.json'))

    print("done; replacing coreferences...")

    count = ITEMS_COUNT
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    replaced = replace_coreferences(raw[:count])

    print("done; writing to {0}/{1} file...".format(TARGET_PATH, TARGET_FILE))

    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)

    json.dump(replaced, open("{0}/{1}".format(TARGET_PATH, TARGET_FILE), "w+"))

    print("done; ready to annotate")


if __name__ == '__main__':
    main()
