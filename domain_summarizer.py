
import os
import json


######################################################################
#   Constant
######################################################################

DS_DD_NAME = 'name'
DS_DD_SIZE = 'size'
DS_DD_FREQ = 'freq'

######################################################################
#   Main Script
######################################################################

class DomainSummarizer(object):

    def __init__(self):
        self.summary = {}

    def init_domain_data(self, domain_name):
        domain = {}
        domain.setdefault(DS_DD_NAME, domain_name)
        domain.setdefault(DS_DD_SIZE, 0)
        domain.setdefault(DS_DD_FREQ, 0)
        self.summary.setdefault(domain_name, domain)

    def load_jsonlines(self, filepath):
        filename = '.'.join(filepath.split(os.path.sep)[-1].split('.')[:-1])
        self.init_domain_data(filename)
        with open(filepath, 'rb') as file_handler:
            for line in file_handler:
                line = line.strip()
                self.summary[filename]



    def load_dir(self, dirpath):
        paths = []
        for subdir, dirs, files in os.walk(dirpath):
            for filename in files:
                if filename[0] == '.' or filename.split('.')[-1] != 'jl':
                    continue
                path = os.path.join(subdir, filename)
                paths.append(path)
        return paths

    def run(self, dirpath):
        paths = self.load_dir(dirpath)
        for path in paths:
            self.load_jsonlines(path)
        print json.dumps(self.summary, indent=4)

if __name__ == '__main__':
    ds = DomainSummarizer()

    dirpath = '/Users/ZwEin/job_works/StudentWork_USC-ISI/projects/domain-summarizer/tests/data'
    ds.run(dirpath)

