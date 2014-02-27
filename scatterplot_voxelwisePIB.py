import pandas as pd
import os, sys
import matplotlib.pyplot as plt
import general_stats as gs
import general_plots as gp
import statsmodels as sm

if __name__ == '__main__':

    datadir = '/home/jagust/rsfmri_ica/results/DualRegress/ROI/voxelwisePIB'
    covfile = os.path.join(datadir, 'ROI_covariates.csv')
    funcfile = os.path.join(datadir,'ROI_fc_intensity.csv')
    dvrfile = os.path.join(datadir,'ROI_dvr_value.csv')
    covariates = ['Age_log','Scanner','Motion_log','pve_GM']
    ##################################################################
    
    covdata = pd.read_csv(covfile, sep='\t')
    funcdata = pd.read_csv(funcfile, sep='\t')
    dvrdata = pd.read_csv(dvrfile, sep='\t')
    old_func = funcdata[funcdata['Group']=='Old']
    old_dvr = dvrdata[dvrdata['Group']=='Old']
    old_cov = covdata[covdata['Group']=='Old']

    for roi in funcdata.columns[2:]:
        outfile = os.path.join(datadir, roi + '.svg')
        outfile = outfile.replace(': ','_')
        df = old_cov.copy()
        df[roi] = old_func[roi]
        df['DVR'] = old_dvr[roi]
        gp.plot_scatter(df, 'DVR', roi, covariates, 
                    outfile, xlabel='PiB DVR (log)', 
                    ylabel='Functional Connectivity', title=roi) 

