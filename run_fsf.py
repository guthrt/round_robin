#!/usr/bin/env ipython

# coding: utf-8

# In[1]:


import os
import glob
import subprocess


# In[2]:


fsfdir = '/projects/csnl/shared/round_robin/analysis/bids_data/fsfs/lev1'


# In[3]:


subdirs = glob.glob("%s/design_sub-G[0-9][0-9]S[0-9][0-9]_run[A-E].fsf"%(fsfdir))
subdirs


# In[ ]:


for dir in list(subdirs):
    sub = dir
    splitdir = dir.split('/')
    splitdir_sub = splitdir[9]
    subnum = splitdir_sub[11:17]
    runnum = splitdir_sub[21]
    fsf_command = "sbatch --job-name %s_%s_feat --partition=short --time 00:60:00 --mem-per-cpu=8G --cpus-per-task=1 -A csnl feat %s"%(subnum,runnum,sub)
    process = subprocess.Popen(fsf_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

