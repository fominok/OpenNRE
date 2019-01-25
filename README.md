# OpenNRE for NLP course, autumn 2018

This repository is a fork of OpenNRE project with additional scripts
to apply it to SemEval2010 dataset and custom dataset built from DBPedia.
Thus, the work can be roughly divided into 2 parts mostly independent:


1. [Applying OpenNRE to SemEval2010](#semeval)
2. [Applying OpenNRE to DBpedia custom dataset](#dbpedia)

## Semeval

### Description

Being unrelated, OpenNRE and SemEval use different format for their datasets, also SemEval's
scorer uses its own format too. The main task for this part is to write converters for formats
used in these tools. 

* `prepare_semeval.sh` is a shell script to automatically download SemEval files, unpack them and prepare 
a compatible dataset
* `create_opennre_dataset.py` is responsible for converting dataset from SemEval format to OpenNRE one;
is is used for train data as well as for test data
* `nre_to_scorer.py` is used after permforming OpenNRE testing to create files compatible with SemEval scorer: 
is uses test data created by `create_opennre_dataset.py` and test results given by OpenNRE's testing script

OpenNRE's format is well described on OpenNRE [GitHub page](https://github.com/thunlp/OpenNRE).

### Evaluation steps

Step 0, remove cache:

    rm -r _processed_data
    
First, we need to setup an environment:

    conda create -n envname --file requirements.txt
    
And activate it:

    conda activate envname
    
    
Provided script will download SemEval 2010 dataset and convert it:

    sh prepare_semeval.sh
    
By default our program use word_vec.json file from NYT dataset, which is mention in head repository of OpenNRE.
Thees word embeddings vectors are built on big corpus that's whu provides good result. We tried to make our own word_vec.json
based on semeval dataset, but because of small size of semeval dataset (only 8 000 sentences) it provides poor results.

To build word_vec file based on semeval dataset run:

    sh prepare_semeval_word_vec.sh
    
Launch training with:

    python train_demo.py semeval pcnn att
    
Wait until it finish or interrupt freely, then test it:

    python test_demo.py semeval pcnn att
    
Another provided script will prepare data and execute SemEval's scorer:

    sh score_semeval.sh

## DBPedia

DBPedia is a project aiming to extract structured content from the information created in the Wikipedia project.

DBPedia provides SPARQL endpoint which allows to query specific data from DBPedia to make some analsysis,
experiments and so on. We used this SPARQL endpoint to download informations about companies (like Google, Coca-Cola etc.)
and its foundation date to train OpenNRE neural network to find relations between company name and foundation date in text.

Our approach in work with DBpedia is taken from [soylent-grin/textext repo](https://github.com/soylent-grin/textext)

From DBpedia we extract:

* dbo:abstract
* dbo:foundingYear
* rdfs:label


This data we store in DBPedia/data/raw.json in intermediate format:

    [
        {
            "abstract": "Auster Aircraft Limited was a British aircraft manufacturer from 1938 to 1961.",
            "company": "Auster",
            "year": "1938"
        },
    ]
    
For better result we replace all coreferences in abstracts, for this case neuralcoref is needed:

Install neuralcoref from repo:

    git clone https://github.com/huggingface/neuralcoref.git
    cd neuralcoref
    pip install -e .
    
Main scripts:

* `dbpedia_load.py` - extracting date from DBPedia by SPARQL endpoint.
* `raw-to-corefered.py $COUNT` - replacing coreferences in abstract. `$COUNT` is number of first raw entries to parse. Default is 1000.
* `create_openNRE_dataset.py` - converting json with DBpedia data to OpenNRE format. It has many config options,
they a described [here](https://github.com/soylent-grin/textext/blob/master/OpenNRE/readme.md#configuration-of-create_opennre_datasetpy).
* `prepare_dbpedia.sh` - automatically run previous three sctipts.
* `score_dbpedia.sh` - runs scorer.pl script which gives marks of classificator worl.
    
Steps for downloading data, replacing coreferences and mapping data format are described in `prepare_dbpedia.sh`,
that's you can just execute it.

    sh prepare_dbpedia.sh
    
Then we can train model:

    python train_demo.py dbpedia pcnn att
    
and

     python test_demo.py dbpedia pcnn att
     
Result:

    [TEST] auc: 0.5818072533499661
    
Prepare data and execute SemEval's scorer on dbpedia model:

    sh score_semeval.sh


## Scores

Here are some results based on Semeval's scorer

| Dataset | Parameters | Word_Vec | F1     | Tags          |
|---------|------------|----------|--------|---------------|
| Semeval | pcnn att   | NYT      | 66.67% | with tags     |
| Semeval | birnn att  | NYT      | 58.65% | with tags     |
| Semeval | pcnn att   | NYT      | 77.24% | without tags  |
| Semeval | pcnn att   | Semeval  | 58.40% | without tags |
| DBPedia | pcnn att   | Texext   | 80.25%  | without tags  |

NYT - [NYT10 Dataset](https://github.com/thunlp/OpenNRE#nyt10-dataset)

Semeval - Created on [semeval dataset](https://github.com/davidsbatista/Annotated-Semantic-Relationships-Datasets#semeval-2010)

Texext - word_vec stealed from [soylent-grin/textext](https://github.com/soylent-grin/textext/tree/master/OpenNRE) repo. But them stealed it from NYT dataset.

Tags column says about special tags in training dataset. Originally semeval data looks like this:

    3 "The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code."
    Instrument-Agency(e2,e1)
    
And in the beginning of our work we didn't remove tags `<e1>` and `<e2>`. Only after they were removed
result made better.

## Problems

### DBPedia

Coreference replacing works not wery well. Sometimes it replaces pronouns not only with company name, but also with some data after company name (espaccialy text in brackets). Here program thought that comapny name is `Lantis Company, Limited (\u682a\u5f0f\u4f1a\u793e\u30e9\u30f3\u30c6\u30a3\u30b9 Kabushiki-gaisha Rantisu)`:

    {
        "abstract": "Lantis Company, Limited (\u682a\u5f0f\u4f1a\u793e\u30e9\u30f3\u30c6\u30a3\u30b9 Kabushiki-gaisha Rantisu) is a Japanese company that specializes as a music publisher label for Japanese musicians, anime soundtracks and video game soundtracks.
            Lantis Company, Limited (\u682a\u5f0f\u4f1a\u793e\u30e9\u30f3\u30c6\u30a3\u30b9 Kabushiki-gaisha Rantisu) was established on November 26, 1999, and in May 2006,
            Lantis Company, Limited (\u682a\u5f0f\u4f1a\u793e\u30e9\u30f3\u30c6\u30a3\u30b9 Kabushiki-gaisha Rantisu) was bought by, and became a subsidiary of, Bandai Visual.
            Lantis Company, Limited (\u682a\u5f0f\u4f1a\u793e\u30e9\u30f3\u30c6\u30a3\u30b9 Kabushiki-gaisha Rantisu) is now a subsidiary of Bandai Namco Holdings.",
        "company": "Lantis (company)",
        "year": "1999"
    },
    
Our program get only year of foundation date and miss everything about day and month. It was done only for simplicity, but is not the best solution.

There are some problems with `demo_test.py`, it provides `score: NaN`. To prevent this some changes were made in script like [here](https://github.com/thunlp/OpenNRE/issues/89) were adviced. 

    _weights_matrix with np.ones(..) instead of np.zeros()
    
It was not fixed in OpenNRE repository yet.
