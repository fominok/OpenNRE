#!/bin/sh

LINK=https://github.com/davidsbatista/Annotated-Semantic-Relationships-Datasets/raw/master/datasets/SemEval2010_task8_all_data.tar.gz
SE_FILE=semeval.tar.gz
SE_TEMP=semeval_temp
SE_DATASET=data/semeval
SE_TEST=semeval_test

wget -O $SE_FILE $LINK

mkdir -p $SE_TEMP
mkdir -p $SE_DATASET
mkdir -p $SE_TEST

cd $SE_TEMP
tar xf ../$SE_FILE
mv SemEval2010_task8_all_data/SemEval2010_task8_training/TRAIN_FILE.TXT train.txt
mv SemEval2010_task8_all_data/SemEval2010_task8_testing_keys/TEST_FILE_FULL.TXT test.txt
mv SemEval2010_task8_all_data/SemEval2010_task8_scorer-v1.2/semeval2010_task8_scorer-v1.2.pl scorer.pl
rm -rf SemEval2010_task8_all_data
cd ..

rm $SE_FILE

mv $SE_TEMP/scorer.pl $SE_TEST/

python3 create_opennre_dataset.py $SE_TEMP/train.txt
mv train.json $SE_DATASET/
mv rel2id.json $SE_DATASET/

python3 create_opennre_dataset.py $SE_TEMP/test.txt
mv train.json $SE_DATASET/test.json
rm rel2id.json

cp word_vec.json $SE_DATASET/
