import re
import sys

import gensim
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


# to init nltk uncomment this for first launch
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')


def train_model(sents):
    return gensim.models.Word2Vec(sents, min_count=2, size=50, workers=4, window=10, iter=25)


class SentencesProvider:
    def __init__(self, path):
        self.path = path
        self.sentence_pattern = re.compile('^[0-9]+\t\"(.+)\"$')
        self.sentence_count = 0
        self.sentences = []
        self.load_sentences()

    def get_sentence(self, line):
        match = self.sentence_pattern.match(line)
        if match is None:
            return None

        return match.group(1)

    def load_sentences(self):
        wordnet_lemmatizer = WordNetLemmatizer()
        sentences = []

        with open(self.path, 'r', encoding='utf8') as f:
            for line in f:
                sentence = self.get_sentence(line)
                if sentence is None:
                    continue
                self.sentence_count += 1
                clean_sentence = BeautifulSoup(sentence, 'html.parser').get_text()
                tokens = word_tokenize(clean_sentence)
                tokens = [t.lower() for t in tokens]
                words = list(filter(lambda s: s.isalpha() and s not in stopwords.words('english'), tokens))
                # words = gensim.utils.simple_preprocess(clean_sentence)
                sentences.append(words)

        self.sentences = sentences


def main():
    loader = SentencesProvider(sys.argv[1])
    model = train_model(loader.sentences)
    print(f'Sentences count used: {loader.sentence_count}')
    model.wv.save_word2vec_format("word2vec.model", binary=False)  # text / vec format


if __name__ == '__main__':
    main()
