#!/bin/sh

LINK=https://github.com/davidsbatista/Annotated-Semantic-Relationships-Datasets/raw/master/datasets/SemEval2010_task8_all_data.tar.gz
SE_FILE=semeval.tar.gz
SE_TEMP=semeval_temp
SE_DATASET=data/semeval
SE_TEST=semeval_test

# Download SemEval2010 dataset
wget -O $SE_FILE $LINK

mkdir -p $SE_TEMP
mkdir -p $SE_DATASET
mkdir -p $SE_TEST

# Extract SemEval dataset with simplified names
cd $SE_TEMP
tar xf ../$SE_FILE
mv SemEval2010_task8_all_data/SemEval2010_task8_training/TRAIN_FILE.TXT train.txt
mv SemEval2010_task8_all_data/SemEval2010_task8_testing_keys/TEST_FILE_FULL.TXT test.txt
mv SemEval2010_task8_all_data/SemEval2010_task8_scorer-v1.2/semeval2010_task8_scorer-v1.2.pl scorer.pl
rm -rf SemEval2010_task8_all_data
cd ..
mv $SE_TEMP/scorer.pl $SE_TEST/
rm $SE_FILE

echo "prepare train data"
python3 create_opennre_dataset.py $SE_TEMP/train.txt

echo "prepare word2vec"
python3 create_word_embedding_model.py $SE_TEMP/train.txt
python3 create_opennre_emb.py word2vec.model

mv new.json $SE_DATASET/word_vec.json
mv train.json $SE_DATASET/
mv rel2id.json $SE_DATASET/

echo "prepare test data"
python3 create_opennre_dataset.py $SE_TEMP/test.txt
mv train.json $SE_DATASET/test.json
rm rel2id.json
rm word2vec.model

mkdir test_result
