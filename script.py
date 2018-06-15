from tqdm import tqdm
import os
import random
import subprocess
from itertools import product

random.seed(1234)

class RandomTrainer:
    def __init__(self, script, random_seed_arg, model_prefix_arg, save_path_arg, log_dir, model_dir, round_num):
        self.script = script
        self.random_seed_arg = random_seed_arg
        self.model_prefix_arg = model_prefix_arg
        self.save_path_arg = save_path_arg
        self.log_dir = log_dir
        self.model_dir = model_dir
        self.round_num = round_num
        os.makedirs(log_dir, exist_ok=True)
        os.makedirs(model_dir, exist_ok=True)

    def start(self, process_num=1):
        process_list = []
        for i in range(self.round_num):
            gen_random = random.randint(0, 65535)
            print(i, gen_random)
            with open(os.path.join(self.log_dir, "{}_{}.log".format(i, gen_random)), "w") as handler:
                if len(process_list) >= process_num:
                    exit_codes = [p.wait() for p in process_list]
                    process_list = []
                proc = subprocess.Popen(
                    self.script.split() +
                    [
                        self.random_seed_arg, str(gen_random),
                        self.model_prefix_arg, "{}_{}".format(i, gen_random),
                        self.save_path_arg, self.model_dir
                    ], stdout=handler)
                process_list.append(proc)


class RandomTester:
    def __init__(self, log_dir):
        self.pipeline = []
        self.ranges = []
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    def add_pipeline(self, script, model_arg, result_parser, log_dir, model_dir, ignore_last, limit=None):
        self.pipeline.append((script, model_arg, result_parser, log_dir, model_dir, ignore_last, limit))

    def add_specific_step(self, script):
        self.pipeline.append((script,))

    def start(self):
        for x in self.pipeline:
            if len(x) == 1:
                self.ranges.append([x[0]])
            else:
                model_lists = sorted(filter(lambda f: f != "." and f != "..", os.listdir(x[4])),
                                   key=lambda f:int(f.split('_')[0]))
                if x[-2]:
                    model_lists = model_lists[:-1]
                if x[-1] is not None:
                    model_lists = model_lists[:x[-1]]
                scripts = []
                for model_file in model_lists:
                    script = "{} {} {}".format(x[0], x[1], os.path.join(x[4], model_file))
                    scripts.append(script)
                self.ranges.append(scripts)
        for idx, pipeline in tqdm(enumerate(product(*self.ranges))):
            # Simple version of pipeline
            # TODO: make it save time
            print(pipeline)
            with open(os.path.join(self.log_dir, "{}.log".format(idx)), 'a+') as handler:
                for cmd in pipeline:
                    subprocess.run(cmd.split(), stdout=handler)

    def parse_results(self, parser):
        results = []
        for file in os.listdir(self.log_dir):
            if file.endswith('log'):
                text = open(os.path.join(self.log_dir, file)).readlines()
                results.append(parser(text))
        return results