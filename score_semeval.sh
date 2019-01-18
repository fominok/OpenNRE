python3 nre_to_scorer.py semeval

mv answer_keys.txt semeval_test/
mv proposed_anwsers.txt semeval_test/

cd semeval_test
./scorer.pl proposed_anwsers.txt answer_keys.txt
