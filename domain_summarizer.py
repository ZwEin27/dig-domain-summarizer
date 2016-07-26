
import os
import json

class DomainSummarizer(object):

    def __init__(self):
        pass

    def load_jsonlines(self, filepath):
        pass

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

if __name__ == '__main__':
    ds = DomainSummarizer()

    dirpath = '/Users/ZwEin/job_works/StudentWork_USC-ISI/projects/dig-data/sample-datasets/escorts/sipsap/clusters/cluster001'
    ds.run(dirpath)

