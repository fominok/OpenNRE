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
    
## Updated results (removing tags)

    <<< (2*9+1)-WAY EVALUATION (USING DIRECTIONALITY)>>>:

    Confusion matrix:
            C-E1 C-W1 C-C1 E-D1 E-O1 I-A1 M-C1 M-T1 P-P1  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
     C-E1 | 307    2    0    2    4    0    1    7    3    0 |  326    0  326
     C-W1 |   2  239    5    1    3   12   20    9   11    0 |  302    0  302
     C-C1 |   0    7  160   11    3    0    1    1    0    0 |  183    0  183
     E-D1 |   1    2   14  271    1    0    0    0    3    0 |  292    0  292
     E-O1 |   3    4    3    9  219    3    2    1    7    0 |  251    0  251
     I-A1 |   3   14    0    5    3  102    1    2   26    0 |  156    0  156
     M-C1 |   1    4    1    3    3    0  207    1    6    0 |  226    0  226
     M-T1 |   1    6    1    1    3    1    2  236   10    0 |  261    0  261
     P-P1 |   9   10    0    3    7   19    3    6  168    0 |  225    0  225
      _O_ |  43   67   31   84   49   12   42   68   54    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  370  355  215  390  295  149  279  331  288    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Wrong) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Other) = 1909/2672 = 71.44%

    Results for the individual relations:
          Cause-Effect(e1,e2) :    P =  307/ 370 =  82.97%     R =  307/ 326 =  94.17%     F1 =  88.22%
       Component-Whole(e1,e2) :    P =  239/ 355 =  67.32%     R =  239/ 302 =  79.14%     F1 =  72.75%
     Content-Container(e1,e2) :    P =  160/ 215 =  74.42%     R =  160/ 183 =  87.43%     F1 =  80.40%
    Entity-Destination(e1,e2) :    P =  271/ 390 =  69.49%     R =  271/ 292 =  92.81%     F1 =  79.47%
         Entity-Origin(e1,e2) :    P =  219/ 295 =  74.24%     R =  219/ 251 =  87.25%     F1 =  80.22%
     Instrument-Agency(e1,e2) :    P =  102/ 149 =  68.46%     R =  102/ 156 =  65.38%     F1 =  66.89%
     Member-Collection(e1,e2) :    P =  207/ 279 =  74.19%     R =  207/ 226 =  91.59%     F1 =  81.98%
         Message-Topic(e1,e2) :    P =  236/ 331 =  71.30%     R =  236/ 261 =  90.42%     F1 =  79.73%
      Product-Producer(e1,e2) :    P =  168/ 288 =  58.33%     R =  168/ 225 =  74.67%     F1 =  65.50%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1909/2672 =  71.44%     R = 1909/2222 =  85.91%     F1 =  78.01%

    MACRO-averaged result (excluding Other):
    P =  71.19%	R =  84.76%	F1 =  77.24%



    <<< (9+1)-WAY EVALUATION IGNORING DIRECTIONALITY >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
      C-E | 307    2    0    2    4    0    1    7    3    0 |  326    0  326
      C-W |   2  239    5    1    3   12   20    9   11    0 |  302    0  302
      C-C |   0    7  160   11    3    0    1    1    0    0 |  183    0  183
      E-D |   1    2   14  271    1    0    0    0    3    0 |  292    0  292
      E-O |   3    4    3    9  219    3    2    1    7    0 |  251    0  251
      I-A |   3   14    0    5    3  102    1    2   26    0 |  156    0  156
      M-C |   1    4    1    3    3    0  207    1    6    0 |  226    0  226
      M-T |   1    6    1    1    3    1    2  236   10    0 |  261    0  261
      P-P |   9   10    0    3    7   19    3    6  168    0 |  225    0  225
      _O_ |  43   67   31   84   49   12   42   68   54    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  370  355  215  390  295  149  279  331  288    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Wrong) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Other) = 1909/2672 = 71.44%

    Results for the individual relations:
                 Cause-Effect :    P =  307/ 370 =  82.97%     R =  307/ 326 =  94.17%     F1 =  88.22%
              Component-Whole :    P =  239/ 355 =  67.32%     R =  239/ 302 =  79.14%     F1 =  72.75%
            Content-Container :    P =  160/ 215 =  74.42%     R =  160/ 183 =  87.43%     F1 =  80.40%
           Entity-Destination :    P =  271/ 390 =  69.49%     R =  271/ 292 =  92.81%     F1 =  79.47%
                Entity-Origin :    P =  219/ 295 =  74.24%     R =  219/ 251 =  87.25%     F1 =  80.22%
            Instrument-Agency :    P =  102/ 149 =  68.46%     R =  102/ 156 =  65.38%     F1 =  66.89%
            Member-Collection :    P =  207/ 279 =  74.19%     R =  207/ 226 =  91.59%     F1 =  81.98%
                Message-Topic :    P =  236/ 331 =  71.30%     R =  236/ 261 =  90.42%     F1 =  79.73%
             Product-Producer :    P =  168/ 288 =  58.33%     R =  168/ 225 =  74.67%     F1 =  65.50%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1909/2672 =  71.44%     R = 1909/2222 =  85.91%     F1 =  78.01%

    MACRO-averaged result (excluding Other):
    P =  71.19%	R =  84.76%	F1 =  77.24%



    <<< (9+1)-WAY EVALUATION TAKING DIRECTIONALITY INTO ACCOUNT -- OFFICIAL >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- xDIRx skip  ACTUAL
      C-E | 307    2    0    2    4    0    1    7    3    0 |  326     0     0    326
      C-W |   2  239    5    1    3   12   20    9   11    0 |  302     0     0    302
      C-C |   0    7  160   11    3    0    1    1    0    0 |  183     0     0    183
      E-D |   1    2   14  271    1    0    0    0    3    0 |  292     0     0    292
      E-O |   3    4    3    9  219    3    2    1    7    0 |  251     0     0    251
      I-A |   3   14    0    5    3  102    1    2   26    0 |  156     0     0    156
      M-C |   1    4    1    3    3    0  207    1    6    0 |  226     0     0    226
      M-T |   1    6    1    1    3    1    2  236   10    0 |  261     0     0    261
      P-P |   9   10    0    3    7   19    3    6  168    0 |  225     0     0    225
      _O_ |  43   67   31   84   49   12   42   68   54    0 |  450     0     0    450
          +--------------------------------------------------+
     -SUM-  370  355  215  390  295  149  279  331  288    0   2672     0     0   2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Wrong) = 1909/2672 = 71.44%
    Accuracy (considering all skipped examples as Other) = 1909/2672 = 71.44%

    Results for the individual relations:
                 Cause-Effect :    P =  307/( 370 +   0) =  82.97%     R =  307/ 326 =  94.17%     F1 =  88.22%
              Component-Whole :    P =  239/( 355 +   0) =  67.32%     R =  239/ 302 =  79.14%     F1 =  72.75%
            Content-Container :    P =  160/( 215 +   0) =  74.42%     R =  160/ 183 =  87.43%     F1 =  80.40%
           Entity-Destination :    P =  271/( 390 +   0) =  69.49%     R =  271/ 292 =  92.81%     F1 =  79.47%
                Entity-Origin :    P =  219/( 295 +   0) =  74.24%     R =  219/ 251 =  87.25%     F1 =  80.22%
            Instrument-Agency :    P =  102/( 149 +   0) =  68.46%     R =  102/ 156 =  65.38%     F1 =  66.89%
            Member-Collection :    P =  207/( 279 +   0) =  74.19%     R =  207/ 226 =  91.59%     F1 =  81.98%
                Message-Topic :    P =  236/( 331 +   0) =  71.30%     R =  236/ 261 =  90.42%     F1 =  79.73%
             Product-Producer :    P =  168/( 288 +   0) =  58.33%     R =  168/ 225 =  74.67%     F1 =  65.50%
                       _Other :    P =    0/(   0 +   0) =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1909/2672 =  71.44%     R = 1909/2222 =  85.91%     F1 =  78.01%

    MACRO-averaged result (excluding Other):
    P =  71.19%	R =  84.76%	F1 =  77.24%



    <<< The official score is (9+1)-way evaluation with directionality taken into account: macro-averaged F1 = 77.24% >>>

        
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

birnn score:

    <<< (2*9+1)-WAY EVALUATION (USING DIRECTIONALITY)>>>:

    Confusion matrix:
            C-E1 C-W1 C-C1 E-D1 E-O1 I-A1 M-C1 M-T1 P-P1  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
     C-E1 | 250   14    2    2   30    6    6    2   14    0 |  326    0  326
     C-W1 |  17  183    5    7   12   22   28   13   15    0 |  302    0  302
     C-C1 |   3   21  117    8   10    6    7    4    7    0 |  183    0  183
     E-D1 |   3   10    7  247    2    4    4    7    8    0 |  292    0  292
     E-O1 |  14   19    3    5  170    2   10    9   19    0 |  251    0  251
     I-A1 |   4   26    2    7   11   80    6    8   12    0 |  156    0  156
     M-C1 |   8   21    4    5   21    5  140   11   11    0 |  226    0  226
     M-T1 |   7   35    3    3    8    3   17  167   18    0 |  261    0  261
     P-P1 |  14   26    3    7   21   16   17   20  101    0 |  225    0  225
      _O_ |  35   86   27   68   40   27   62   56   49    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  355  441  173  359  325  171  297  297  254    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Wrong) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Other) = 1455/2672 = 54.45%

    Results for the individual relations:
          Cause-Effect(e1,e2) :    P =  250/ 355 =  70.42%     R =  250/ 326 =  76.69%     F1 =  73.42%
       Component-Whole(e1,e2) :    P =  183/ 441 =  41.50%     R =  183/ 302 =  60.60%     F1 =  49.26%
     Content-Container(e1,e2) :    P =  117/ 173 =  67.63%     R =  117/ 183 =  63.93%     F1 =  65.73%
    Entity-Destination(e1,e2) :    P =  247/ 359 =  68.80%     R =  247/ 292 =  84.59%     F1 =  75.88%
         Entity-Origin(e1,e2) :    P =  170/ 325 =  52.31%     R =  170/ 251 =  67.73%     F1 =  59.03%
     Instrument-Agency(e1,e2) :    P =   80/ 171 =  46.78%     R =   80/ 156 =  51.28%     F1 =  48.93%
     Member-Collection(e1,e2) :    P =  140/ 297 =  47.14%     R =  140/ 226 =  61.95%     F1 =  53.54%
         Message-Topic(e1,e2) :    P =  167/ 297 =  56.23%     R =  167/ 261 =  63.98%     F1 =  59.86%
      Product-Producer(e1,e2) :    P =  101/ 254 =  39.76%     R =  101/ 225 =  44.89%     F1 =  42.17%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1455/2672 =  54.45%     R = 1455/2222 =  65.48%     F1 =  59.46%

    MACRO-averaged result (excluding Other):
    P =  54.51%	R =  63.96%	F1 =  58.65%



    <<< (9+1)-WAY EVALUATION IGNORING DIRECTIONALITY >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
      C-E | 250   14    2    2   30    6    6    2   14    0 |  326    0  326
      C-W |  17  183    5    7   12   22   28   13   15    0 |  302    0  302
      C-C |   3   21  117    8   10    6    7    4    7    0 |  183    0  183
      E-D |   3   10    7  247    2    4    4    7    8    0 |  292    0  292
      E-O |  14   19    3    5  170    2   10    9   19    0 |  251    0  251
      I-A |   4   26    2    7   11   80    6    8   12    0 |  156    0  156
      M-C |   8   21    4    5   21    5  140   11   11    0 |  226    0  226
      M-T |   7   35    3    3    8    3   17  167   18    0 |  261    0  261
      P-P |  14   26    3    7   21   16   17   20  101    0 |  225    0  225
      _O_ |  35   86   27   68   40   27   62   56   49    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  355  441  173  359  325  171  297  297  254    0   2672    0 2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Wrong) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Other) = 1455/2672 = 54.45%

    Results for the individual relations:
                 Cause-Effect :    P =  250/ 355 =  70.42%     R =  250/ 326 =  76.69%     F1 =  73.42%
              Component-Whole :    P =  183/ 441 =  41.50%     R =  183/ 302 =  60.60%     F1 =  49.26%
            Content-Container :    P =  117/ 173 =  67.63%     R =  117/ 183 =  63.93%     F1 =  65.73%
           Entity-Destination :    P =  247/ 359 =  68.80%     R =  247/ 292 =  84.59%     F1 =  75.88%
                Entity-Origin :    P =  170/ 325 =  52.31%     R =  170/ 251 =  67.73%     F1 =  59.03%
            Instrument-Agency :    P =   80/ 171 =  46.78%     R =   80/ 156 =  51.28%     F1 =  48.93%
            Member-Collection :    P =  140/ 297 =  47.14%     R =  140/ 226 =  61.95%     F1 =  53.54%
                Message-Topic :    P =  167/ 297 =  56.23%     R =  167/ 261 =  63.98%     F1 =  59.86%
             Product-Producer :    P =  101/ 254 =  39.76%     R =  101/ 225 =  44.89%     F1 =  42.17%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1455/2672 =  54.45%     R = 1455/2222 =  65.48%     F1 =  59.46%

    MACRO-averaged result (excluding Other):
    P =  54.51%	R =  63.96%	F1 =  58.65%



    <<< (9+1)-WAY EVALUATION TAKING DIRECTIONALITY INTO ACCOUNT -- OFFICIAL >>>:

    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- xDIRx skip  ACTUAL
      C-E | 250   14    2    2   30    6    6    2   14    0 |  326     0     0    326
      C-W |  17  183    5    7   12   22   28   13   15    0 |  302     0     0    302
      C-C |   3   21  117    8   10    6    7    4    7    0 |  183     0     0    183
      E-D |   3   10    7  247    2    4    4    7    8    0 |  292     0     0    292
      E-O |  14   19    3    5  170    2   10    9   19    0 |  251     0     0    251
      I-A |   4   26    2    7   11   80    6    8   12    0 |  156     0     0    156
      M-C |   8   21    4    5   21    5  140   11   11    0 |  226     0     0    226
      M-T |   7   35    3    3    8    3   17  167   18    0 |  261     0     0    261
      P-P |  14   26    3    7   21   16   17   20  101    0 |  225     0     0    225
      _O_ |  35   86   27   68   40   27   62   56   49    0 |  450     0     0    450
          +--------------------------------------------------+
     -SUM-  355  441  173  359  325  171  297  297  254    0   2672     0     0   2672

    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Wrong) = 1455/2672 = 54.45%
    Accuracy (considering all skipped examples as Other) = 1455/2672 = 54.45%

    Results for the individual relations:
                 Cause-Effect :    P =  250/( 355 +   0) =  70.42%     R =  250/ 326 =  76.69%     F1 =  73.42%
              Component-Whole :    P =  183/( 441 +   0) =  41.50%     R =  183/ 302 =  60.60%     F1 =  49.26%
            Content-Container :    P =  117/( 173 +   0) =  67.63%     R =  117/ 183 =  63.93%     F1 =  65.73%
           Entity-Destination :    P =  247/( 359 +   0) =  68.80%     R =  247/ 292 =  84.59%     F1 =  75.88%
                Entity-Origin :    P =  170/( 325 +   0) =  52.31%     R =  170/ 251 =  67.73%     F1 =  59.03%
            Instrument-Agency :    P =   80/( 171 +   0) =  46.78%     R =   80/ 156 =  51.28%     F1 =  48.93%
            Member-Collection :    P =  140/( 297 +   0) =  47.14%     R =  140/ 226 =  61.95%     F1 =  53.54%
                Message-Topic :    P =  167/( 297 +   0) =  56.23%     R =  167/ 261 =  63.98%     F1 =  59.86%
             Product-Producer :    P =  101/( 254 +   0) =  39.76%     R =  101/ 225 =  44.89%     F1 =  42.17%
                       _Other :    P =    0/(   0 +   0) =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%

    Micro-averaged result (excluding Other):
    P = 1455/2672 =  54.45%     R = 1455/2222 =  65.48%     F1 =  59.46%

    MACRO-averaged result (excluding Other):
    P =  54.51%	R =  63.96%	F1 =  58.65%



    <<< The official score is (9+1)-way evaluation with directionality taken into account: macro-averaged F1 = 58.65% >>>

