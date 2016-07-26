# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-26 17:41:20

import os
import sys
import time
import json
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from domain_summarizer import DomainSummarizer

class TestMethods(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_run(self):
        ds = DomainSummarizer()
        ds.run(TEST_DATA_DIR)
            
if __name__ == '__main__':
    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestMethods('test_run'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

