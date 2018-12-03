# OpenNRE for NLP course, autumn 2018

Step 0, remove cache:

    rm -r _processed_data
    
First, we need to setup an environment:

    conda create -n envname --file requirements.txt
    
And activate it:

    conda activate envname
    
    
Provided script will download SemEval 2010 dataset and convert it:

    sh prepare_semeval.sh
    
Launch training with:

    python train_demo.py semeval pcnn att
    
Wait until it finish or interrupt freely, then test it:

    python test_demo.py semeval pcnn att
    
Another provided script will prepare data and execute SemEval's scorer:

    sh score_semeval.sh
