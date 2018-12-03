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
    
Example:


    <<< (2*9+1)-WAY EVALUATION (USING DIRECTIONALITY)>>>:

    Confusion matrix:
            C-E1 C-W1 C-C1 E-D1 E-O1 I-A1 M-C1 M-T1 P-P1  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
     C-E1 | 274    2    1    4   22    6    1    3   13    0 |  326    0  326
     C-W1 |   7  199    6   10   11   26   17   13   13    0 |  302    0  302
     C-C1 |   0   11  156    8    3    0    1    3    1    0 |  183    0  183
     E-D1 |   0    4   10  269    2    3    1    2    1    0 |  292    0  292
     E-O1 |   8   13    3    6  205    4    2    2    8    0 |  251    0  251
     I-A1 |   2   22    5    7    6   79    6   10   19    0 |  156    0  156
     M-C1 |   1   15    2    4    9    0  181    9    5    0 |  226    0  226
     M-T1 |   3   20    1    5   10    3   16  177   26    0 |  261    0  261
     P-P1 |  14   18    5    5   10   22   18   10  123    0 |  225    0  225
      _O_ |  22   69   32   67   50   47   60   52   51    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  331  373  221  385  328  190  303  281  260    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Wrong) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Other) = 1663/2672 = 62.24%

    Results for the individual relations:
          Cause-Effect(e1,e2) :    P =  274/ 331 =  82.78%     R =  274/ 326 =  84.05%     F1 =  83.41%
       Component-Whole(e1,e2) :    P =  199/ 373 =  53.35%     R =  199/ 302 =  65.89%     F1 =  58.96%
     Content-Container(e1,e2) :    P =  156/ 221 =  70.59%     R =  156/ 183 =  85.25%     F1 =  77.23%
    Entity-Destination(e1,e2) :    P =  269/ 385 =  69.87%     R =  269/ 292 =  92.12%     F1 =  79.47%
         Entity-Origin(e1,e2) :    P =  205/ 328 =  62.50%     R =  205/ 251 =  81.67%     F1 =  70.81%
     Instrument-Agency(e1,e2) :    P =   79/ 190 =  41.58%     R =   79/ 156 =  50.64%     F1 =  45.66%
     Member-Collection(e1,e2) :    P =  181/ 303 =  59.74%     R =  181/ 226 =  80.09%     F1 =  68.43%
         Message-Topic(e1,e2) :    P =  177/ 281 =  62.99%     R =  177/ 261 =  67.82%     F1 =  65.31%
      Product-Producer(e1,e2) :    P =  123/ 260 =  47.31%     R =  123/ 225 =  54.67%     F1 =  50.72%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1663/2672 =  62.24%     R = 1663/2222 =  74.84%     F1 =  67.96%

    MACRO-averaged result (excluding Other):
    P =  61.19%	R =  73.58%	F1 =  66.67%



    <<< (9+1)-WAY EVALUATION IGNORING DIRECTIONALITY >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
      C-E | 274    2    1    4   22    6    1    3   13    0 |  326    0  326
      C-W |   7  199    6   10   11   26   17   13   13    0 |  302    0  302
      C-C |   0   11  156    8    3    0    1    3    1    0 |  183    0  183
      E-D |   0    4   10  269    2    3    1    2    1    0 |  292    0  292
      E-O |   8   13    3    6  205    4    2    2    8    0 |  251    0  251
      I-A |   2   22    5    7    6   79    6   10   19    0 |  156    0  156
      M-C |   1   15    2    4    9    0  181    9    5    0 |  226    0  226
      M-T |   3   20    1    5   10    3   16  177   26    0 |  261    0  261
      P-P |  14   18    5    5   10   22   18   10  123    0 |  225    0  225
      _O_ |  22   69   32   67   50   47   60   52   51    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  331  373  221  385  328  190  303  281  260    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Wrong) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Other) = 1663/2672 = 62.24%

    Results for the individual relations:
                 Cause-Effect :    P =  274/ 331 =  82.78%     R =  274/ 326 =  84.05%     F1 =  83.41%
              Component-Whole :    P =  199/ 373 =  53.35%     R =  199/ 302 =  65.89%     F1 =  58.96%
            Content-Container :    P =  156/ 221 =  70.59%     R =  156/ 183 =  85.25%     F1 =  77.23%
           Entity-Destination :    P =  269/ 385 =  69.87%     R =  269/ 292 =  92.12%     F1 =  79.47%
                Entity-Origin :    P =  205/ 328 =  62.50%     R =  205/ 251 =  81.67%     F1 =  70.81%
            Instrument-Agency :    P =   79/ 190 =  41.58%     R =   79/ 156 =  50.64%     F1 =  45.66%
            Member-Collection :    P =  181/ 303 =  59.74%     R =  181/ 226 =  80.09%     F1 =  68.43%
                Message-Topic :    P =  177/ 281 =  62.99%     R =  177/ 261 =  67.82%     F1 =  65.31%
             Product-Producer :    P =  123/ 260 =  47.31%     R =  123/ 225 =  54.67%     F1 =  50.72%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1663/2672 =  62.24%     R = 1663/2222 =  74.84%     F1 =  67.96%

    MACRO-averaged result (excluding Other):
    P =  61.19%	R =  73.58%	F1 =  66.67%



    <<< (9+1)-WAY EVALUATION TAKING DIRECTIONALITY INTO ACCOUNT -- OFFICIAL >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- xDIRx skip  ACTUAL
      C-E | 274    2    1    4   22    6    1    3   13    0 |  326     0     0    326
      C-W |   7  199    6   10   11   26   17   13   13    0 |  302     0     0    302
      C-C |   0   11  156    8    3    0    1    3    1    0 |  183     0     0    183
      E-D |   0    4   10  269    2    3    1    2    1    0 |  292     0     0    292
      E-O |   8   13    3    6  205    4    2    2    8    0 |  251     0     0    251
      I-A |   2   22    5    7    6   79    6   10   19    0 |  156     0     0    156
      M-C |   1   15    2    4    9    0  181    9    5    0 |  226     0     0    226
      M-T |   3   20    1    5   10    3   16  177   26    0 |  261     0     0    261
      P-P |  14   18    5    5   10   22   18   10  123    0 |  225     0     0    225
      _O_ |  22   69   32   67   50   47   60   52   51    0 |  450     0     0    450
          +--------------------------------------------------+
     -SUM-  331  373  221  385  328  190  303  281  260    0   2672     0     0   2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Wrong) = 1663/2672 = 62.24%
    Accuracy (considering all skipped examples as Other) = 1663/2672 = 62.24%

    Results for the individual relations:
                 Cause-Effect :    P =  274/( 331 +   0) =  82.78%     R =  274/ 326 =  84.05%     F1 =  83.41%
              Component-Whole :    P =  199/( 373 +   0) =  53.35%     R =  199/ 302 =  65.89%     F1 =  58.96%
            Content-Container :    P =  156/( 221 +   0) =  70.59%     R =  156/ 183 =  85.25%     F1 =  77.23%
           Entity-Destination :    P =  269/( 385 +   0) =  69.87%     R =  269/ 292 =  92.12%     F1 =  79.47%
                Entity-Origin :    P =  205/( 328 +   0) =  62.50%     R =  205/ 251 =  81.67%     F1 =  70.81%
            Instrument-Agency :    P =   79/( 190 +   0) =  41.58%     R =   79/ 156 =  50.64%     F1 =  45.66%
            Member-Collection :    P =  181/( 303 +   0) =  59.74%     R =  181/ 226 =  80.09%     F1 =  68.43%
                Message-Topic :    P =  177/( 281 +   0) =  62.99%     R =  177/ 261 =  67.82%     F1 =  65.31%
             Product-Producer :    P =  123/( 260 +   0) =  47.31%     R =  123/ 225 =  54.67%     F1 =  50.72%
                       _Other :    P =    0/(   0 +   0) =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1663/2672 =  62.24%     R = 1663/2222 =  74.84%     F1 =  67.96%

    MACRO-averaged result (excluding Other):
    P =  61.19%	R =  73.58%	F1 =  66.67%



    <<< The official score is (9+1)-way evaluation with directionality taken into account: macro-averaged F1 = 66.67% >>>
