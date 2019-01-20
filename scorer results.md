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
    
    
We tried to build our own word_vec.json file from words in semeval dataset, in chance to improve result.
But word_vec.json from Semeval dataset brought worse result. The main reason of it is small size of semeval dataset:
and NYTs train.json is 636MB, Train.json from the Semeval corpus is only 2.44 MB.

Result from scorer.pl:

    <<< (2*9+1)-WAY EVALUATION (USING DIRECTIONALITY)>>>:
    
    Confusion matrix:
            C-E1 C-E2 C-W1 C-W2 C-C1 C-C2 E-D1 E-D2 E-O1 E-O2 I-A1 I-A2 M-C1 M-C2 M-T1 M-T2 P-P1 P-P2  _O_ <-- classified as
          +-----------------------------------------------------------------------------------------------+ -SUM- skip ACTUAL
     C-E1 | 114    0    1    0    0    0    2    0    6    0    0    0    1    0    6    0    4    0    0 |  134    0  134
     C-E2 |   0  176    0    0    0    0    0    0    0    0    0    0    0    5    0    0    0   11    0 |  192    0  192
     C-W1 |   2    0  100    0    6    0   16    0   12    0    1    0    0    0    4    0    6    0    0 |  147    0  147
     C-W2 |   0    4    0   69    0    1    0    3    0   15    0   21    0   27    0    1    0   14    0 |  155    0  155
     C-C1 |   0    0   23    0   84    0   32    0    6    0    0    0    0    0    0    0    0    0    0 |  145    0  145
     C-C2 |   0    0    0    8    0   26    0    1    0    0    0    2    0    1    0    0    0    0    0 |   38    0   38
     E-D1 |   0    0    8    0   22    0  227    0   18    0    0    0    2    0    5    0    8    0    0 |  290    0  290
     E-D2 |   0    0    0    1    0    0    0    0    0    0    0    0    0    1    0    0    0    0    0 |    2    0    2
     E-O1 |   9    0   24    0    2    0   18    0  112    0    1    0    0    0   15    0   22    0    0 |  203    0  203
     E-O2 |   0    0    0    9    0    0    0    2    0   17    0    3    0    5    0    1    0   11    0 |   48    0   48
     I-A1 |   0    0    4    0    0    0    1    0    7    0    2    0    1    0    7    0    2    0    0 |   24    0   24
     I-A2 |   0    1    0   17    0    0    0    4    0    3    0   70    0   17    0    2    0   18    0 |  132    0  132
     M-C1 |   0    0    9    0    0    0    3    0    8    0    0    0    1    0    0    0    5    0    0 |   26    0   26
     M-C2 |   0    2    0    9    0    0    0    2    0    2    0    4    0  171    0    1    0    9    0 |  200    0  200
     M-T1 |   1    0   11    0    0    0    8    0   20    0    1    0    2    0  145    0   21    0    0 |  209    0  209
     M-T2 |   0    0    0    2    0    0    0    1    0    0    0    6    0    5    0   22    0   16    0 |   52    0   52
     P-P1 |   8    0   13    0    0    0    6    0   23    0    1    0    1    0   17    0   35    0    0 |  104    0  104
     P-P2 |   0    1    0   15    0    0    0    4    0    0    0   14    0   13    0    5    0   69    0 |  121    0  121
      _O_ |  10    0   68    0   15    0   95    1  106    0   11    0    9    0   72    1   60    2    0 |  450    0  450
          +-----------------------------------------------------------------------------------------------+
     -SUM-  144  184  261  130  129   27  408   18  318   37   17  120   17  245  271   33  163  150    0   2672    0 2672
    
    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Wrong) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Other) = 1440/2672 = 53.89%
    
    Results for the individual relations:
          Cause-Effect(e1,e2) :    P =  114/ 144 =  79.17%     R =  114/ 134 =  85.07%     F1 =  82.01%
          Cause-Effect(e2,e1) :    P =  176/ 184 =  95.65%     R =  176/ 192 =  91.67%     F1 =  93.62%
       Component-Whole(e1,e2) :    P =  100/ 261 =  38.31%     R =  100/ 147 =  68.03%     F1 =  49.02%
       Component-Whole(e2,e1) :    P =   69/ 130 =  53.08%     R =   69/ 155 =  44.52%     F1 =  48.42%
     Content-Container(e1,e2) :    P =   84/ 129 =  65.12%     R =   84/ 145 =  57.93%     F1 =  61.31%
     Content-Container(e2,e1) :    P =   26/  27 =  96.30%     R =   26/  38 =  68.42%     F1 =  80.00%
    Entity-Destination(e1,e2) :    P =  227/ 408 =  55.64%     R =  227/ 290 =  78.28%     F1 =  65.04%
    Entity-Destination(e2,e1) :    P =    0/  18 =   0.00%     R =    0/   2 =   0.00%     F1 =   0.00%
         Entity-Origin(e1,e2) :    P =  112/ 318 =  35.22%     R =  112/ 203 =  55.17%     F1 =  42.99%
         Entity-Origin(e2,e1) :    P =   17/  37 =  45.95%     R =   17/  48 =  35.42%     F1 =  40.00%
     Instrument-Agency(e1,e2) :    P =    2/  17 =  11.76%     R =    2/  24 =   8.33%     F1 =   9.76%
     Instrument-Agency(e2,e1) :    P =   70/ 120 =  58.33%     R =   70/ 132 =  53.03%     F1 =  55.56%
     Member-Collection(e1,e2) :    P =    1/  17 =   5.88%     R =    1/  26 =   3.85%     F1 =   4.65%
     Member-Collection(e2,e1) :    P =  171/ 245 =  69.80%     R =  171/ 200 =  85.50%     F1 =  76.85%
         Message-Topic(e1,e2) :    P =  145/ 271 =  53.51%     R =  145/ 209 =  69.38%     F1 =  60.42%
         Message-Topic(e2,e1) :    P =   22/  33 =  66.67%     R =   22/  52 =  42.31%     F1 =  51.76%
      Product-Producer(e1,e2) :    P =   35/ 163 =  21.47%     R =   35/ 104 =  33.65%     F1 =  26.22%
      Product-Producer(e2,e1) :    P =   69/ 150 =  46.00%     R =   69/ 121 =  57.02%     F1 =  50.92%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%
    
    Micro-averaged result (excluding Other):
    P = 1440/2672 =  53.89%     R = 1440/2222 =  64.81%     F1 =  58.85%
    
    MACRO-averaged result (excluding Other):
    P =  49.88%	R =  52.09%	F1 =  49.92%
    
    
    
    <<< (9+1)-WAY EVALUATION IGNORING DIRECTIONALITY >>>:
    
    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- skip ACTUAL
      C-E | 290    1    0    2    6    0    6    6   15    0 |  326    0  326
      C-W |   6  169    7   19   27   22   27    5   20    0 |  302    0  302
      C-C |   0   31  110   33    6    2    1    0    0    0 |  183    0  183
      E-D |   0    9   22  227   18    0    3    5    8    0 |  292    0  292
      E-O |   9   33    2   20  129    4    5   16   33    0 |  251    0  251
      I-A |   1   21    0    5   10   72   18    9   20    0 |  156    0  156
      M-C |   2   18    0    5   10    4  172    1   14    0 |  226    0  226
      M-T |   1   13    0    9   20    7    7  167   37    0 |  261    0  261
      P-P |   9   28    0   10   23   15   14   22  104    0 |  225    0  225
      _O_ |  10   68   15   96  106   11    9   73   62    0 |  450    0  450
          +--------------------------------------------------+
     -SUM-  328  391  156  426  355  137  262  304  313    0   2672    0 2672
    
    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Wrong) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Other) = 1440/2672 = 53.89%
    
    Results for the individual relations:
                 Cause-Effect :    P =  290/ 328 =  88.41%     R =  290/ 326 =  88.96%     F1 =  88.69%
              Component-Whole :    P =  169/ 391 =  43.22%     R =  169/ 302 =  55.96%     F1 =  48.77%
            Content-Container :    P =  110/ 156 =  70.51%     R =  110/ 183 =  60.11%     F1 =  64.90%
           Entity-Destination :    P =  227/ 426 =  53.29%     R =  227/ 292 =  77.74%     F1 =  63.23%
                Entity-Origin :    P =  129/ 355 =  36.34%     R =  129/ 251 =  51.39%     F1 =  42.57%
            Instrument-Agency :    P =   72/ 137 =  52.55%     R =   72/ 156 =  46.15%     F1 =  49.15%
            Member-Collection :    P =  172/ 262 =  65.65%     R =  172/ 226 =  76.11%     F1 =  70.49%
                Message-Topic :    P =  167/ 304 =  54.93%     R =  167/ 261 =  63.98%     F1 =  59.12%
             Product-Producer :    P =  104/ 313 =  33.23%     R =  104/ 225 =  46.22%     F1 =  38.66%
                       _Other :    P =    0/   0 =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%
    
    Micro-averaged result (excluding Other):
    P = 1440/2672 =  53.89%     R = 1440/2222 =  64.81%     F1 =  58.85%
    
    MACRO-averaged result (excluding Other):
    P =  55.35%	R =  62.96%	F1 =  58.40%
    
    
    
    <<< (9+1)-WAY EVALUATION TAKING DIRECTIONALITY INTO ACCOUNT -- OFFICIAL >>>:
    
    Confusion matrix:
             C-E  C-W  C-C  E-D  E-O  I-A  M-C  M-T  P-P  _O_ <-- classified as
          +--------------------------------------------------+ -SUM- xDIRx skip  ACTUAL
      C-E | 290    1    0    2    6    0    6    6   15    0 |  326     0     0    326
      C-W |   6  169    7   19   27   22   27    5   20    0 |  302     0     0    302
      C-C |   0   31  110   33    6    2    1    0    0    0 |  183     0     0    183
      E-D |   0    9   22  227   18    0    3    5    8    0 |  292     0     0    292
      E-O |   9   33    2   20  129    4    5   16   33    0 |  251     0     0    251
      I-A |   1   21    0    5   10   72   18    9   20    0 |  156     0     0    156
      M-C |   2   18    0    5   10    4  172    1   14    0 |  226     0     0    226
      M-T |   1   13    0    9   20    7    7  167   37    0 |  261     0     0    261
      P-P |   9   28    0   10   23   15   14   22  104    0 |  225     0     0    225
      _O_ |  10   68   15   96  106   11    9   73   62    0 |  450     0     0    450
          +--------------------------------------------------+
     -SUM-  328  391  156  426  355  137  262  304  313    0   2672     0     0   2672
    
    Coverage = 2672/2672 = 100.00%
    Accuracy (calculated for the above confusion matrix) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Wrong) = 1440/2672 = 53.89%
    Accuracy (considering all skipped examples as Other) = 1440/2672 = 53.89%
    
    Results for the individual relations:
                 Cause-Effect :    P =  290/( 328 +   0) =  88.41%     R =  290/ 326 =  88.96%     F1 =  88.69%
              Component-Whole :    P =  169/( 391 +   0) =  43.22%     R =  169/ 302 =  55.96%     F1 =  48.77%
            Content-Container :    P =  110/( 156 +   0) =  70.51%     R =  110/ 183 =  60.11%     F1 =  64.90%
           Entity-Destination :    P =  227/( 426 +   0) =  53.29%     R =  227/ 292 =  77.74%     F1 =  63.23%
                Entity-Origin :    P =  129/( 355 +   0) =  36.34%     R =  129/ 251 =  51.39%     F1 =  42.57%
            Instrument-Agency :    P =   72/( 137 +   0) =  52.55%     R =   72/ 156 =  46.15%     F1 =  49.15%
            Member-Collection :    P =  172/( 262 +   0) =  65.65%     R =  172/ 226 =  76.11%     F1 =  70.49%
                Message-Topic :    P =  167/( 304 +   0) =  54.93%     R =  167/ 261 =  63.98%     F1 =  59.12%
             Product-Producer :    P =  104/( 313 +   0) =  33.23%     R =  104/ 225 =  46.22%     F1 =  38.66%
                       _Other :    P =    0/(   0 +   0) =   0.00%     R =    0/ 450 =   0.00%     F1 =   0.00%
    
    Micro-averaged result (excluding Other):
    P = 1440/2672 =  53.89%     R = 1440/2222 =  64.81%     F1 =  58.85%
    
    MACRO-averaged result (excluding Other):
    P =  55.35%	R =  62.96%	F1 =  58.40%
    
    
    
    <<< The official score is (9+1)-way evaluation with directionality taken into account: macro-averaged F1 = 58.40% >>>