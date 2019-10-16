import os
import glob
import subprocess
import re

studydir = '/projects/csnl/shared/round_robin/analysis/target_analysis'

fmap_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/fmap/my_fieldmap_rads.nii.gz"%(studydir))

for dir in list(fmap_subdirs): 
    sub = dir 
    fmap_path = re.findall('.*fmap/', sub)[0]
    subfile = 'my_fieldmap_rads'
    new_subfile = '%s/%s1'%(fmap_path, subfile)
    split_command = 'fslsplit %s %s -t'%(sub, new_subfile) 
    process = subprocess.Popen(split_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
