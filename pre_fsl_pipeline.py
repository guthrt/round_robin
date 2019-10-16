
# coding: utf-8

# In[1]:


import os
import glob
import subprocess
import numpy as np 
import json
import re


# In[2]:


#Edit this section with the path to the bids data directory
studydir = '/projects/csnl/shared/round_robin/analysis/target_valence_analysis'


# In[3]:


#Make a list of all the paths to the T1w images for each subject for brain extraction
anat_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/anat/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_T1w.nii.gz"%(studydir))

#Make a list of all the paths to the ap and the pa fieldmap images for each subject for fieldmap creation
fmap_ap_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/fmap/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_dir-ap_epi.nii.gz"%(studydir))
fmap_pa_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/fmap/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_dir-pa_epi.nii.gz"%(studydir))

#Make a list of all the paths to each functional RR run (A-E) json files for slice timing extraction
func_subdirs = glob.glob("%s/sub-G[0-9][0-9]S[0-9][0-9]/ses-wave1/func/sub-G[0-9][0-9]S[0-9][0-9]_ses-wave1_task-RR_aq-[A-E]_bold.json"%(studydir))


# In[4]:


#Go through the list of T1w images for each subject and first run ssroi on them and then run bet2 on the ssroi image for brain extraction
for dir in list(anat_subdirs):
    anat_path = re.findall('.*anat/', dir)[0]
    original = re.findall('sub-G[0-9][0-9]S0[0-9]_ses.*.gz', dir)[0]
    same = re.findall('sub-G[0-9][0-9]S0[0-9]_ses.*_T1w', dir)[0]
    ssr_output = '%s%s_ssroi.nii.gz'%(anat_path, same)
    ssr_command = "standard_space_roi %s%s %s -b"%(anat_path, original, ssr_output)
    process = subprocess.Popen(ssr_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bet_output = "%s%s_brain.nii.gz"%(anat_path, same)
    bet_command = "bet2 %s %s -f .2 -m"%(ssr_output, bet_output)
    process = subprocess.Popen(bet_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


# In[5]:


#For each subject: 
#merge the ap and pa fieldmap images 
#create a datain text file (2 rows of 4 numbers) with first 3 being encoding direction (ap first - 0 -1 0) and last number total readout time of func image
#run topup to create a fieldmap in degrees and an se_epi_unwarped image
#convert fieldmap from degrees to radians 
#use se_epi_unwarped to calculate magnitude image
#run brain extraction on the magnitude image 
#my_fieldmap_rads and my_fieldmap_mag_brain used in fsl feat gui
subdirs_len = len(fmap_ap_subdirs)
for x in range(subdirs_len):
    ap_path = fmap_ap_subdirs[x]
    pa_path = fmap_pa_subdirs[x]
    subfile = re.findall('sub-G[0-9][0-9]S0[0-9]_ses.*ap.*.gz', ap_path)[0]
    fmap_path = re.findall('.*fmap/', ap_path)[0]
    new_start = subfile[0:20]
    new_end = '_merged_fmap.nii.gz'
    new = '%s%s%s'%(fmap_path, new_start, new_end)
    merge_command = 'fslmerge -t %s %s %s'%(new, ap_path, pa_path)
    process = subprocess.Popen(merge_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    text_name = 'datain.txt'
    file_location = '%s%s'%(fmap_path, text_name)
    with open(file_location, "w+") as file:
        file.write("0 -1 0 0.0355\n0 1 0 0.0355")
    top_up_command = 'topup --imain=%s --datain=%s --config=b02b0.cnf --fout=%smy_fieldmap --iout=%sse_epi_unwarped'%(new, file_location, fmap_path, fmap_path)
    process = subprocess.Popen(top_up_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    rads_command = 'fslmaths %smy_fieldmap -mul 6.28 %smy_fieldmap_rads'%(fmap_path, fmap_path)
    process = subprocess.Popen(rads_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    mag_command = 'fslmaths %sse_epi_unwarped -Tmean %smy_fieldmap_mag'%(fmap_path, fmap_path)
    process = subprocess.Popen(mag_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bet_command = 'bet2 %smy_fieldmap_mag %smy_fieldmap_mag_brain'%(fmap_path, fmap_path)
    process = subprocess.Popen(bet_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


# In[12]:


#load in the json files for each run (A-E) for each subject, pull the slice timing and create a slice time text file for each run
for dir in list(func_subdirs):
    sub = dir
    func_path = re.findall('.*func/', sub)[0]
    runnum = re.findall('aq-([A-E])', sub)[0]
    with open(sub) as f:
        dicto = json.load(f)
    slice_time = dicto['SliceTiming']
    file_name = 'slice_time_run%s.txt'%(runnum)
    file_location = '%s%s'%(func_path,file_name)
    with open(file_location, 'w+') as file:
        for listitem in slice_time:
            file.write('%s\n' % listitem)
            
            

