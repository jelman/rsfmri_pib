#!/bin/sh
#Registers pre-processed functional data to standard space using existing warp

for subj in `cat /home/jagust/jelman/rsfmri_ica/Spreadsheets/Filelists/allsubs.txt`
do


fsl_sub applywarp --ref=/home/jagust/jelman/templates/MNI152_T1_3mm_brain.nii.gz \
--in=/home/jagust/rsfmri_ica/GIFT/data/"$subj"_Preproc.feat/filtered_func_data.nii.gz \
--out=/home/jagust/rsfmri_ica/GIFT/data/"$subj"_Preproc.feat/"$subj"_func2standard.nii.gz \
--warp=/home/jagust/rsfmri_ica/data/"$subj"/func/"$subj"_4d_OldYoungICA.ica/reg/example_func2standard_warp.nii.gz

done
