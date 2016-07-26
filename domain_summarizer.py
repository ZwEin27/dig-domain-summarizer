
"""
python domain_summarizer.py -d <DOMAINS_DIR> -o <OUTPUT_FILE>

"""


import os
import json


######################################################################
#   Constant
######################################################################

# DS_DD_NAME = 'name'
DS_DD_SIZE = 'size'
# DS_DD_FREQ = 'freq'

DS_BIN_BASE = 128

######################################################################
#   Main Script
######################################################################

class DomainSummarizer(object):

    def __init__(self):
        self.summary = {}

    def fit_bin_size(self, domain_dict, size):
        offset = 0
        cap = DS_BIN_BASE
        while cap < size:
            cap = cap << 1
        domain_dict[DS_DD_SIZE].setdefault(cap, 0)
        domain_dict[DS_DD_SIZE][cap] += 1

    def init_domain_data(self, domain_name):
        domain = {}
        # domain.setdefault(DS_DD_NAME, domain_name)
        domain.setdefault(DS_DD_SIZE, {})
        # domain.setdefault(DS_DD_FREQ, 0)
       
        self.summary.setdefault(domain_name, domain)

    def update_domain_data(self, domain_name, data):
        size = len(data)
        self.fit_bin_size(self.summary[domain_name], size)

        # self.summary[domain_name][DS_DD_SIZE]
        # self.summary[domain_name][DS_DD_FREQ]


    def load_jsonlines(self, filepath):
        domain_name = '.'.join(filepath.split(os.path.sep)[-1].split('.')[:-1])
        print 'process domain:', domain_name
        self.init_domain_data(domain_name)
        with open(filepath, 'rb') as file_handler:
            for line in file_handler:
                line = line.strip().encode('ascii', 'ignore')
                self.update_domain_data(domain_name, line)

    def load_dir(self, dirpath):
        paths = []
        for subdir, dirs, files in os.walk(dirpath):
            for filename in files:
                if filename[0] == '.' or filename.split('.')[-1] != 'jl':
                    continue
                path = os.path.join(subdir, filename)
                paths.append(path)
        return paths

    def run(self, dirpath, output_path=None):
        paths = self.load_dir(dirpath)
        for path in paths:
            self.load_jsonlines(path)

        # currently focus size
        ans = {k:v[DS_DD_SIZE] for (k, v) in self.summary.iteritems()}

        if output_path:
            with open(output_path, 'wb') as file_handler:
                file_handler.write(json.dumps(ans, indent=4))
        else:
            print json.dumps(ans, indent=4)
        return ans

if __name__ == '__main__':
    # ds = DomainSummarizer()
    # dirpath = '/Users/ZwEin/job_works/StudentWork_USC-ISI/projects/domain-summarizer/tests/data'
    # ds.run(dirpath)
    
    import sys
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d','--dirpath', required=True)
    arg_parser.add_argument('-o','--output_path', required=False)

    args = arg_parser.parse_args()

    dirpath = args.dirpath
    output_path = args.output_path

    ds = DomainSummarizer()
    ds.run(dirpath, output_path=output_path)


    
