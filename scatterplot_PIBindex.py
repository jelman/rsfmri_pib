import pandas as pd
import os, sys
import matplotlib.pyplot as plt
import general_stats as gs
import general_plots as gp
import statsmodels as sm

if __name__ == '__main__':

    ####################### Set parameters ###########################
    datadir = '/home/jagust/rsfmri_ica/results/DualRegress/ROI/PIB_Index'
    infile = os.path.join(datadir,'ROI_Data.csv')
    covariates = ['Age_log','Scanner','Motion_log','pve_GM']
    ##################################################################
    
    data = pd.read_csv(infile, sep=',')
    olddata = data[data['Group']=='Old']
    youngdata = data[data['Group']=='Young']
    
    for roi in data.columns[7:]:
        outfile = os.path.join(datadir, roi + '.jpg')
        outfile = outfile.replace(': ','_')
        gp.plot_scatter(olddata, 'PIB_Index_log', roi, covariates, 
                    outfile, xlabel='PiB Index (log)', 
                    ylabel='Functional Connectivity', title=roi) 
