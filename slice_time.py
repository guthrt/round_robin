import os
import glob
import subprocess
import numpy as np 
import json
import re

#Edit this section with the path to the bids data directory
studydir = '/projects/csnl/shared/round_robin/analysis/RSA_analysis'

#Make a list of all the paths to each functional RR run (A-E) json files for slice timing extraction
func_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/func/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_task-RR_aq-[A-E]_bold.json"%(studydir))

for dir in list(func_subdirs):
    sub = dir
    func_path = re.findall('.*func/', dir)[0]
    run_num = re.findall('aq-([A-E])', dir)[0]
    with open(sub) as f:
        dicto = json.load(f)
    slice_time = dicto['SliceTiming']
    file_name = 'slice_time_run%s.txt'%(run_num)
    file_location = '%s%s'%(func_path,file_name)
    with open(file_location, 'w+') as file:
        for listitem in slice_time:
            file.write('%s\n' % listitem)
