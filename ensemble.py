import script
import argparse
import os
from collections import defaultdict
import math
import subprocess

argparser = argparse.ArgumentParser()
argparser.add_argument("--train_dataset", default="123", type=str)
argparser.add_argument("--log_dir", default="attn_ave_123_log", type=str)
args = argparser.parse_args()


P30_list = []
MAP_list = []
PID_list = []
best_map = 0
best_p30 = 0
best = 0
for path in os.listdir(args.log_dir):
    if not "log" in path:
        continue
    fin = open(os.path.join(args.log_dir, path))
    pid = None
    p30_score = 0
    map_score = 0
    lines = fin.readlines()
    line = lines[-4]
    pid = line.strip()
    PID_list.append(pid)
    line = lines[-1]
    items = line.strip().split('\t')
    if "test" == items[0] and "ACC" in items[1] and "P30" in items[2]:
        p30_score = float(items[2].split(":")[1])
        map_score = float(items[3].split(":")[1])
    line = lines[-2]
    items = line.strip().split('\t')
    valid_p30 = float(items[2].split(":")[1])
    if valid_p30 > best:
        best = valid_p30
        best_p30 = p30_score
        best_map = map_score
    MAP_list.append(map_score)
    P30_list.append(p30_score)


def ensemble(dataset="valid"):
    results = defaultdict(list)
    ensemble_results = []
    length = 0
    size = len(PID_list)
    for pid in PID_list:
        fin = open("pred.{}.{}".format(dataset, pid))
        results[pid] = fin.readlines()
        length = len(results[pid])
    for i in range(length):
        score = 0
        qid = 0
        docid = 0
        for pid in PID_list:
            items = results[pid][i].strip().split()
            s = math.exp(float(items[4]))
            qid = items[0]
            docid = items[2]
            score += s
        ensemble_results.append("{} Q0 {} 0 {} NN\n".format(qid, docid, score / size))
    fout = open(os.path.join(args.log_dir, "pred.{}.ensemble".format(dataset)),"w")
    for line in ensemble_results:
        fout.write(line)
    fout.flush()
    fout.close()

    trec_eval_path = 'trec_eval-9.0.5/trec_eval'
    gold_fname = "data/qrels.txt"
    pred_fname = os.path.join(args.log_dir, "pred.{}.ensemble".format(dataset))
    trec_out = subprocess.check_output([trec_eval_path, gold_fname, pred_fname])
    trec_out_lines = str(trec_out, 'utf-8').split('\n')
    mean_average_precision = float(trec_out_lines[5].split('\t')[-1])
    p_30 = float(trec_out_lines[25].split('\t')[-1])
    return mean_average_precision, p_30

average_map = sum(MAP_list)/ len(MAP_list)
average_p30 = sum(P30_list)/ len(P30_list)
max_map = max(MAP_list)
min_map = min(MAP_list)
max_p30 = max(P30_list)
min_p30 = min(P30_list)
print("Test results")
print("Average MAP {} P30 {}".format(average_map, average_p30))
print("Max MAP {} {}  P30 {} {}".format(max_map, max_map - average_map, max_p30, max_p30 - average_p30))
print("Min MAP {} {}  P30 {} {}".format(min_map, min_map - average_map, min_p30, min_p30 - average_p30))

print("Best results: MAP {} P30 {} ".format(best_map, best_p30))

print("Ensemble Results")
valid_mean_average_precision, valid_p_30 = ensemble(dataset="valid")
print("Ensemble: MAP {} P30 {}".format(valid_mean_average_precision, valid_p_30))
test_mean_average_precision, test_p_30 = ensemble(dataset="test")
print("Ensemble: MAP {} P30 {}".format(test_mean_average_precision, test_p_30))

