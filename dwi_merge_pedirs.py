import numpy as np
import os
import glob
import subprocess

here = os.getcwd()
path = '/projects/csnl/shared/round_robin/analysis/target_analysis'
subs = glob.glob(path + '/sub-*')
names = [sub.split('/')[-1] for sub in subs]
subs = [sub + '/ses-wave1/dwi/' for sub in subs]
for sub,name in zip(subs,names):

	if os.path.exists(os.path.join(sub,name + '_merged.nii.gz')): continue 
	
	print(name)
	# bvals
	rl = np.loadtxt(os.path.join(sub,name + '_ses-wave1_RL_MR.bval'))
	lr = np.loadtxt(os.path.join(sub,name + '_ses-wave1_LR_MR.bval'))
	bval = np.concatenate((rl,lr))
	np.savetxt(os.path.join(sub,name + '_merged.bval'),bval)

	# bvecs
	rl_vec = np.loadtxt(os.path.join(sub,name + '_ses-wave1_RL_MR.bvec'))
	lr_vec = np.loadtxt(os.path.join(sub,name + '_ses-wave1_LR_MR.bvec'))
	bvec = np.concatenate((rl_vec,lr_vec),axis=1)
	np.savetxt(os.path.join(sub,name + '_merged.bvec'),bvec)

	# niftis
	rl_nifti = os.path.join(sub,name + '_ses-wave1_RL_MR.nii.gz')
	lr_nifti = os.path.join(sub,name + '_ses-wave1_LR_MR.nii.gz')
	os.chdir(sub)
	with open(os.path.join(sub,name + '_merge.srun'),'w') as f:
		f.write("""#!/bin/bash  \n #SBATCH  --job-name %s_dwi \n  
			#SBATCH --partition=short \nfslmerge -t %s %s %s"""%(name,os.path.join(sub,name+'_merged.nii.gz'),rl_nifti,lr_nifti))
	
	#merge_command = "sbatch --job-name %s_dwi --partition=short  --cpus-per-task=1 -A csnl fslmerge -t  %s %s %s"%(name,os.path.join(sub,name+'_merged.nii.gz'),rl_nifti,lr_nifti)
	#print(merge_command)
	#os.popen(merge_command)
	os.system('sbatch -A csnl {}'.format(name+ '_merge.srun'))
	os.system('rm {}'.format(name+'_merge.srun'))
	os.system('rm slurm*')
	#process = subprocess.Popen(merge_command.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()
#	os.system('rm {}'.format(name+ '_merge.py'))

