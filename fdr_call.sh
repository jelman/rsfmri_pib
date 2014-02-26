#!/bin/sh

datadir=/home/jagust/jelman/rsfmri_ica/data/OldICA_IC0_ecat_2mm_6fwhm_125.gica
#for i in 01 10 14 24 12 08 04 29 39 30 16 36 24 05 06 03 49; #7mm-70
#for i in 00 14 17 19 13 08 04 16 40 36 11 45 22 45; #5mm
#for i in 00 01 03 05 07 08 10 11 13 14 16 21 22 #8mm
#for i in 00 01 02 03 04 05 06 07 08 09 10 11 12 13; #Grecius
for i in 00 01 04 05 07 08 09 10 11 12; #6mm
do

let j=$((10#$i))+1

#fdr -i "$datadir"/randomise/TwoSamp_GM_ic00"$i"_vox_p_tstat1.nii.gz --oneminusp -m "$datadir"/masks/netmask00"$i".nii.gz -q 0.05 --othresh="$datadir"/randomise/TwoSamp_GM_ic00"$i"_fdr_corrp_tstat1

#fdr -i "$datadir"/randomise/TwoSamp_GM_ic00"$i"_vox_p_tstat2.nii.gz --oneminusp -m "$datadir"/masks/netmask00"$i".nii.gz -q 0.05 --othresh="$datadir"/randomise/TwoSamp_GM_ic00"$i"_fdr_corrp_tstat2

#fdr -i "$datadir"/randomise/TwoSamp_GM_ic00"$i"_vox_p_tstat3.nii.gz --oneminusp -m "$datadir"/masks/netmask00"$i".nii.gz -q 0.05 --othresh="$datadir"/randomise/TwoSamp_GM_ic00"$i"_fdr_corrp_tstat3

fdr -i "$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_vox_p_tstat1.nii.gz --oneminusp -m "$datadir"/masks/DR_GMmask_pibsubs.nii.gz -q 0.05 -o "$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_fdr_qrate_tstat1 --othresh="$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_fdr_corrp_tstat1

fdr -i "$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_vox_p_tstat2.nii.gz --oneminusp -m "$datadir"/masks/DR_GMmask_pibsubs.nii.gz -q 0.05 -o "$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_fdr_qrate_tstat2 --othresh="$datadir"/randomise/VoxelwisePIB_GMvoxel_DRmask/VoxelwisePIB_GM_ic00"$i"_fdr_corrp_tstat2




done
