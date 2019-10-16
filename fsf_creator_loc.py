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


subdirs = glob.glob("%s/sub-G05S05/ses-wave1/func/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_task-loc_bold.nii.gz"%(studydir))
subdirs


# In[18]:


for dir in list(subdirs):
    subnum =  re.findall('sub-(G[0-9][0-9]S0[0-9])/', dir)[0]
    runnum = 'loc'
    groupnum = subnum[2]
    sub = subnum[:3] + '_' + subnum[3:]
    replacements = {'SUBNUM':subnum, 'RUNNUM':runnum, 'GROUPNUM':groupnum, 'SUB':sub}
    with open("%s/lev1_loc/template.fsf"%(fsfdir)) as infile:
        with open("%s/lev1_loc/design_sub-%s_loc.fsf"%(fsfdir, subnum), 'w') as outfile:
            for line in infile:
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)
