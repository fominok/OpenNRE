# OpenNRE for NLP course, autumn 2018

First, we need to setup an environment:

    conda create -n envname --file requirements.txt
    
And activate it:

    conda activate envname
    
    
Provided script will download SemEval 2010 dataset and convert it:

    sh prepare_semeval.sh
    
Launch training with:

    python train_demo.py semeval pcnn att
