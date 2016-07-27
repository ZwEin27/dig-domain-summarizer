# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-26 19:09:30
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-26 19:23:33

import json

filepath = 'domain_summarizer_output_cdr_input_files.json'
with open(filepath, 'rb') as file_handler:
    ans = {}
    ans.setdefault('bin_size', {})
    ans.setdefault('bin_size_detail', {})

    json_obj = json.load(file_handler)
    for domain_name, size_dict in json_obj.iteritems():
        for bin_size, count in size_dict.iteritems():
            ans['bin_size'].setdefault(str(bin_size), 0)
            ans['bin_size'][str(bin_size)] += count

            ans['bin_size_detail'].setdefault(str(bin_size), {})
            ans['bin_size_detail'][str(bin_size)].setdefault(domain_name, count)

    print json.dumps(ans, indent=4, sort_keys=True)

