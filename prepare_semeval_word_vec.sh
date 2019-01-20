#!/bin/sh

SE_TEMP=semeval_temp
SE_DATASET=data/semeval

echo "prepare word2vec"
python3 create_word_embedding_model.py $SE_TEMP/train.txt
python3 create_opennre_emb.py word2vec.model

mv new.json $SE_DATASET/word_vec.json
rm word2vec.model