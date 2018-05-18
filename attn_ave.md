```
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching python ensemble.py --train_dataset 123 --log_dir eval_attn_ave_123_log
Test results
Average MAP 0.43433 P30 0.6576699999999998
Max MAP 0.4417 0.007369999999999988  P30 0.6727 0.01503000000000021
Min MAP 0.4236 -0.010730000000000017  P30 0.6412 -0.016469999999999763
Best results: MAP 0.4371 P30 0.6624
Ensemble Results
Ensemble: MAP 0.359 P30 0.4744
Ensemble: MAP 0.4409 P30 0.6612
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching python ensemble.py --train_dataset 124 --log_dir eval_attn_ave_124_log
Test results
Average MAP 0.27981 P30 0.51924
Max MAP 0.2828 0.0029899999999999927  P30 0.5256 0.006359999999999921
Min MAP 0.2765 -0.0033099999999999796  P30 0.5139 -0.005340000000000011
Best results: MAP 0.2808 P30 0.5217
Ensemble Results
Ensemble: MAP 0.4023 P30 0.5111
Ensemble: MAP 0.2855 P30 0.5244
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching python ensemble.py --train_dataset 134 --log_dir eval_attn_ave_134_log
Test results
Average MAP 0.23645 P30 0.39001
Max MAP 0.2417 0.005250000000000005  P30 0.4034 0.013389999999999957
Min MAP 0.2292 -0.0072500000000000064  P30 0.3768 -0.01321
Best results: MAP 0.2417 P30 0.3972
Ensemble Results
Ensemble: MAP 0.4522 P30 0.6178
Ensemble: MAP 0.243 P30 0.4051
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching python ensemble.py --train_dataset 234 --log_dir eval_attn_ave_234_log
Test results
Average MAP 0.38993 P30 0.43756000000000006
Max MAP 0.399 0.009070000000000022  P30 0.4483 0.010739999999999916
Min MAP 0.3694 -0.020529999999999993  P30 0.4197 -0.017860000000000043
Best results: MAP 0.3871 P30 0.4435
Ensemble Results
Ensemble: MAP 0.3316 P30 0.54
Ensemble: MAP 0.401 P30 0.4463
```

## 2014
```
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching trec_eval-9.0.5/trec_eval -q data/qrels.txt eval_attn_ave_123_log/pred.test.ensemble > eval_attn_ave_123_log/test.eval
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching perl ../tools/paired-randomization-test-v2.pl -t a  ~/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval
run1name        run2name        metric  run1score       run2score       pctChange       sigLevel
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_10    0.712727        0.758182        6.377551        0.185670
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_100   0.466909        0.482364        3.309969        0.304540
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_1000  0.125564        0.125564        0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_15    0.683631        0.733329        7.269739        0.147860
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_20    0.660909        0.711818        7.702889        0.109300
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_200   0.351909        0.376909        7.104107        0.067020
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_30    0.618189        0.661211        6.959330        0.137680
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_5     0.760000        0.810909        6.698565        0.182800
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval P_500   0.219236        0.232655        6.120418        0.001320
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval Rprec   0.435473        0.469584        7.833076        0.024870
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval bpref   0.415196        0.455347        9.670342        0.011700
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.00    0.874645        0.904538        3.417697        0.218900
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.10    0.758589        0.794475        4.730552        0.135820
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.20    0.653804        0.728267        11.389297       0.001050
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.30    0.577735        0.651155        12.708259       0.009610
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.40    0.490695        0.564273        14.994701       0.003120
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.50    0.400364        0.470749        17.580381       0.005740
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.60    0.296793        0.368902        24.296111       0.000450
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.70    0.206640        0.232062        12.302467       0.197420
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.80    0.148595        0.152976        2.948842        0.846960
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_0.90    0.090342        0.091111        0.851312        0.977280
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval iprec_at_recall_1.00    0.000000        0.000000        0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval map     0.392424        0.440873        12.346119       0.002200
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval num_rel 193.545455      193.545455      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval num_rel_ret     125.563636      125.563636      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval num_ret 755.981818      755.981818      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2014.QL.txt.treceval eval_attn_ave_123_log/test.eval recip_rank      0.833753        0.895913        7.455448        0.044560
```

## 2013
```
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching trec_eval-9.0.5/trec_eval -q data/qrels.txt eval_attn_ave_124_log/pred.test.ensemble > eval_attn_ave_124_log/test.eval
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching perl ../tools/paired-randomization-test-v2.pl -t a  ~/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval
run1name        run2name        metric  run1score       run2score       pctChange       sigLevel
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_10    0.585000        0.663333        13.390313       0.024190
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_100   0.309833        0.351500        13.448090       0.012740
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_1000  0.071767        0.071767        0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_15    0.538892        0.617773        14.637760       0.011060
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_20    0.504167        0.582500        15.537190       0.007270
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_200   0.225000        0.251000        11.555556       0.011730
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_30    0.445005        0.524447        17.851859       0.003930
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_5     0.640000        0.706667        10.416667       0.112300
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval P_500   0.125667        0.134800        7.267905        0.012590
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval Rprec   0.299902        0.327587        9.231359        0.067350
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval bpref   0.283875        0.313035        10.272127       0.066140
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.00    0.821812        0.860607        4.720668        0.237900
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.10    0.613842        0.659793        7.485915        0.167050
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.20    0.500628        0.558232        11.506207       0.110670
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.30    0.368760        0.413717        12.191308       0.096370
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.40    0.275652        0.309322        12.214691       0.114700
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.50    0.202700        0.237178        17.009538       0.096090
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.60    0.156895        0.169293        7.902313        0.508570
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.70    0.096087        0.096807        0.749324        0.957190
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.80    0.060867        0.044960        -26.133625      0.194320
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_0.90    0.004878        0.001733        -64.468739      1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval iprec_at_recall_1.00    0.004167        0.001733        -58.400000      1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval map     0.253200        0.285525        12.766588       0.030750
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval num_rel 150.183333      150.183333      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval num_rel_ret     71.766667       71.766667       0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval num_ret 769.866667      769.866667      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2013.QL.txt.treceval eval_attn_ave_124_log/test.eval recip_rank      0.785357        0.836430        6.503202        0.234750
```

## 2012

```
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching trec_eval-9.0.5/trec_eval -q data/qrels.txt eval_attn_ave_134_log/pred.test.ensemble > eval_attn_ave_134_log/test.eval
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching perl ../tools/paired-randomization-test-v2.pl -t a  ~/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval
run1name        run2name        metric  run1score       run2score       pctChange       sigLevel
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_10    0.416949        0.472881        13.414634       0.066310
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_100   0.239322        0.276780        15.651558       0.045530
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_1000  0.058814        0.058814        0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_15    0.392088        0.464402        18.443190       0.011850
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_20    0.359322        0.446610        24.292453       0.001760
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_200   0.173051        0.198983        14.985309       0.064330
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_30    0.331071        0.405075        22.352712       0.002390
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_5     0.440678        0.511864        16.153846       0.067660
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval P_500   0.099559        0.108407        8.886619        0.021620
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval Rprec   0.266607        0.306464        14.949968       0.026400
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval bpref   0.260981        0.297266        13.903195       0.037310
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.00    0.665988        0.769444        15.534200       0.011850
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.10    0.453753        0.537229        18.396871       0.003330
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.20    0.383225        0.441337        15.163885       0.057880
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.30    0.300553        0.350732        16.695803       0.050110
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.40    0.249619        0.278580        11.602105       0.211040
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.50    0.211512        0.235756        11.462273       0.324610
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.60    0.181117        0.179680        -0.793569       0.948400
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.70    0.101459        0.107273        5.729941        0.697590
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.80    0.041429        0.045188        9.074173        0.718260
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_0.90    0.006605        0.009966        50.885296       0.063320
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval iprec_at_recall_1.00    0.001031        0.001347        30.756579       0.500250
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval map     0.209108        0.242981        16.198713       0.019370
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval num_rel 106.542373      106.542373      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval num_rel_ret     58.813559       58.813559       0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval num_ret 830.474576      830.474576      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2012.QL.txt.treceval eval_attn_ave_134_log/test.eval recip_rank      0.581393        0.731234        25.772691       0.003400
```

## 2011
```
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching trec_eval-9.0.5/trec_eval -q data/qrels.txt eval_attn_ave_234_log/pred.test.ensemble > eval_attn_ave_234_log/test.eval
(PyTorch_0_4_0) ➜  Twitter_Relevance_Matching perl ../tools/paired-randomization-test-v2.pl -t a  ~/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval
run1name        run2name        metric  run1score       run2score       pctChange       sigLevel
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_10    0.500000        0.565306        13.061224       0.017590
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_100   0.256122        0.276327        7.888446        0.219670
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_1000  0.042510        0.042510        0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_15    0.477547        0.529253        10.827443       0.032950
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_20    0.446939        0.502041        12.328767       0.042530
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_200   0.167653        0.178980        6.755934        0.191450
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_30    0.400000        0.446257        11.564286       0.080410
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_5     0.563265        0.640816        13.768116       0.041570
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval P_500   0.078980        0.082939        5.012920        0.233340
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval Rprec   0.393904        0.436173        10.730883       0.076400
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval bpref   0.370355        0.434514        17.323694       0.006000
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.00    0.822937        0.850641        3.366490        0.370430
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.10    0.649206        0.725778        11.794625       0.029700
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.20    0.580898        0.628714        8.231450        0.180300
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.30    0.525065        0.566839        7.955862        0.239620
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.40    0.450120        0.511910        13.727393       0.068870
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.50    0.406978        0.462039        13.529303       0.092520
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.60    0.292678        0.330524        12.931275       0.184380
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.70    0.209722        0.237084        13.046398       0.283970
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.80    0.156016        0.159504        2.235506        0.805850
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_0.90    0.096978        0.098245        1.306846        0.936110
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval iprec_at_recall_1.00    0.033410        0.025553        -23.517195      0.499500
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval map     0.357594        0.401002        12.138956       0.025770
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval num_rel 60.510204       60.510204       0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval num_rel_ret     42.510204       42.510204       0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval num_ret 811.836735      811.836735      0.000000        1.000000
/u1/p8shi/../w85yang/baseline/run.microblog2011.QL.txt.treceval eval_attn_ave_234_log/test.eval recip_rank      0.748857        0.805649        7.583801        0.172760
```
