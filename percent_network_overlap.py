import os, sys
import numpy as np
import general_utilities as utils
from glob import glob
import pandas as pd


def calc_pct_overlap(roi, target):
    roi_nvoxels = roi.sum()
    overlap = (roi==target) * roi
    overlap_nvoxels = overlap.sum()
    return (float(overlap_nvoxels)/float(roi_nvoxels))

if __name__ == '__main__':


    ########### Set parameters ##########
    datadir = '/home/jagust/rsfmri_ica/GIFT/GICA_d30/BPM/results/PIB_Index_log_scaled/Results_ROIs'
    roiglob = os.path.join(datadir,'ic*.nii.gz')
    roi_files = glob(roiglob)
    template = '/home/jagust/rsfmri_ica/GIFT/GICA_d30/network_volumes/netmasks/ic_masks_4D.nii.gz'
    template_mapfile = '/home/jagust/rsfmri_ica/GIFT/GICA_d30/network_volumes/netmasks/template_mapping.txt'
    outfile = os.path.join(datadir, 'Network_Labels_GICA30.csv')
    ####################################

    #Load template and 4D roi data
    tempdat, _ = utils.load_nii(template)
    temp_mapping = utils.load_mapping(template_mapfile)
    # Verify the shape of datasets match


    roi_labels = {}
    for roi in roi_files:
        overlap_dict = {}
        _,roi_name,_ = utils.split_filename(roi)
        roidat, _ = utils.load_nii(roi)
        assert tempdat.shape[:-1] == roidat.shape
        for j in range(tempdat.shape[3]):
            temp_mask = tempdat[:,:,:,j]
            pct_overlap = calc_pct_overlap(roidat, temp_mask)
            net_name = temp_mapping[str(j+1)].split('.')[0]
            overlap_dict[net_name] = pct_overlap
        roi_labels[roi_name] = overlap_dict

    df = pd.DataFrame(roi_labels)
    df.to_csv(outfile, header=True,index_label='Network')
