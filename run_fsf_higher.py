#!/usr/bin/env ipython

# coding: utf-8

# In[1]:


import os
import glob
import subprocess
import re


# In[2]:


fsfdir = '/projects/csnl/shared/round_robin/analysis/target_analysis/fsfs/lev2'


# In[3]:


subdirs = glob.glob("%s/design_sub-G[0-9][0-9]S[0-9][0-9].fsf"%(fsfdir))
subdirs


# In[ ]:


for dir in list(subdirs):
    subnum = re.findall('sub-(G[0-9][0-9]S0[0-9])', dir)[0]
    fsf_command = "sbatch --job-name %s_feat --partition=short --time 00:60:00 --mem-per-cpu=4G --cpus-per-task=1 -A csnl feat %s"%(subnum,dir)
    process = subprocess.Popen(fsf_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

