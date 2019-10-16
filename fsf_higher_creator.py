
# coding: utf-8

# In[14]:


import os
import glob
import re


# In[15]:


studydir = '/projects/csnl/shared/round_robin/analysis/target_analysis/'


# In[16]:


fsfdir = "%s/fsfs"%(studydir)


# In[17]:


subdirs = glob.glob("%s/sub-G05S05/ses-wave1/func/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_task-RR_aq-A_bold.nii.gz"%(studydir))
subdirs


# In[18]:


for dir in list(subdirs):
    sub = dir
    subnum =  re.findall('sub-(G[0-9][0-9]S0[0-9])/', sub)[0]
    replacements = {'SUBNUM':subnum}
    with open("%s/lev2/template.fsf"%(fsfdir)) as infile:
        with open("%s/lev2/design_sub-%s.fsf"%(fsfdir, subnum), 'w') as outfile:
            for line in infile:
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)
    
    
