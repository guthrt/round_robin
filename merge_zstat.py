import os
import glob
import subprocess
import re
import numpy as np


analysis_dir = '/projects/csnl/shared/round_robin/analysis/target_analysis/'

model_dirs = glob.glob('%s/sub-G[0-9][0-9]S0[0-9]/ses-wave1/model/higher.gfeat'%(analysis_dir))

for dir in list(model_dirs):
    sub = dir
    subnum = re.findall('sub-(G[0-9][0-9]S[0-9][0-9])', sub)[0] 
    cope = glob.glob('%s/cope[1-6].feat'%(sub))
    cope = np.array(cope)
    cope.sort()
    if cope.shape[0] < 6:
        continue
    cope1 = cope[0] + "/stats/zstat1.nii.gz"
    cope2 = cope[1] + "/stats/zstat1.nii.gz"
    cope3 = cope[2] + "/stats/zstat1.nii.gz"
    cope4 = cope[3] + "/stats/zstat1.nii.gz"
    cope5 = cope[4] + "/stats/zstat1.nii.gz"        
    cope6 = cope[5] + "/stats/zstat1.nii.gz"
    merge_command = "fslmerge -t %s/merged_stat_maps/%s_merged %s %s %s %s %s %s"%(analysis_dir, subnum, cope1, cope2, cope3, cope4, cope5, cope6)
    process = subprocess.Popen(merge_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
