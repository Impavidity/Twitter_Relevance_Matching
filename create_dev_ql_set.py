from collections import defaultdict

ql_data_collections = defaultdict(list)

folds = ["123", "124", "134", "234"]
ql_files = ["2011", "2012", "2013", "2014"]

for ql_file in ql_files:
    fin = open("baseline/run.microblog{}.QL.txt".format(ql_file))
    for line in fin:
        items = line.strip().split()
        qid = items[0]
        docid = items[2]
        score = items[4]
        ql_data_collections[qid].append((qid, docid, score))



for fold in folds:
    fin = open("data/valid{}.comb".format(fold))
    qid_list = []
    for line in fin:
        items = line.strip().split('\t')
        qid = items[0]
        if qid not in qid_list:
            qid_list.append(qid)
    fout = open("data/run.microblog{}.QL.valid.txt".format(fold), "w")
    for qid in qid_list:
        for item in ql_data_collections[qid]:
            fout.write("{} Q0 {} 0 {} QL\n".format(item[0], item[1], item[2]))
    fout.flush()
    fout.close()


