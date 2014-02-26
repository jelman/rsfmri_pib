import pandas as pd
import os, sys
import matplotlib.pyplot as plt
import general_stats as gs
import general_plots as gp
import statsmodels as sm

if __name__ == '__main__':

    datadir = '/home/jagust/rsfmri_ica/results/DualRegress/ROI/voxelwisePIB'
    covfile = os.path.join(datadir, 'ROI_covariates.csv')
    funcfile = os.path.join(datadir,'ROI_fc_intensity_Old.csv')
    dvrfile = os.path.join(datadir,'ROI_dvr_value_Old.csv')
    covariates = ['Age_log','Scanner','Motion_log','pve_GM']
    ##################################################################
    
    data = pd.read_csv(infile, sep=',')
    olddata = data[data['Group']=='Old']
    youngdata = data[data['Group']=='Young']
    
    for roi in data.columns[7:]:
        outfile = os.path.join(datadir, roi + '.svg')
        gp.plot_scatter(olddata, 'PIB_Index_log', roi, covariates, 
                    outfile, xlabel='PiB Index (log)', 
                    ylabel='Functional Connectivity', title=roi) 
                    
 #############################################################                   
    datadir = '/home/jagust/rsfmri_ica/results/DualRegress/ROI/net_diff'
    covfile = os.path.join(datadir, 'ROI_covariates.csv')
    funcfile = os.path.join(datadir,'ROI_net_split_diff_voxelwisePIB.csv')
    dvrfile = os.path.join(datadir,'ROI_net_split_diff_voxelwisePIB_dvr.csv')
    design_cols = ['PIB_Index_log','Age_log','Scanner','Motion_log','pve_GM']

    
    covdata = gs.load_design(covfile)
    funcdata = pd.read_csv(funcfile, sep='\t')
    dvrdata = pd.read_csv(dvrfile, sep='\t')
    old_idx = covdata['Group']=='Old'
    young_idx = covdata['Group']=='Young'
    all_cov = covdata.drop('Group', axis=1)
    old_cov = all_cov[old_idx]
    young_cov = all_cov[young_idx]
    for roi in funcdata.columns:
        # Load data, create datasets for old and young subjects
        # y = funcdata[roi]
        # old_y = y[old_idx]
        # young_y = y[young_idx]
        # pib = dvrdata[roi]
        # old_pib = pib[old_idx]
        # young_pib = pib[young_idx]
        # # Create design matrix
        # old_x = old_cov.copy()
        # old_x.insert(1, 'PIB_Index_log', old_pib)
        # young_x = young_cov.copy()
        # young_x.insert(1, 'PIB_Index_log', young_pib)       
        # # Regress and plot old subject data
        # old_rlm_results = gs.run_rlm(old_y, old_x)
        # f, ax = plt.subplots()
        # sm.graphics.regressionplots.plot_ccpr(old_rlm_results, 1, ax=ax)
        # ax.set_xlabel('PIB Index (log)')
        # ax.set_ylabel('Adjusted Intensity')
        # ax.set_title(roi)
        # # Regress and get mean value for comparison group (young subjects)
        # young_rlm_results = gs.run_rlm(young_y, young_x)
        # young_y_fitted = (young_x['PIB_Index_log'] * young_rlm_results.params['PIB_Index_log'])
        # young_y_part = young_rlm_results.resid + young_y_fitted
        # young_y_mean = young_y_part.mean()
        # ax.axhline(y=young_y_mean, color='red', linestyle='--',label='Young Subject Mean Intensity')
        # leg = ax.legend(['Old Subjects','Old Subjects\nPartial Regression', 'Young Subjects Mean Intensity'],
        #     loc=0, numpoints=1, prop={'size':10}, markerscale=.8, fancybox=True)
        # leg.get_frame().set_alpha(0.5)
        # outfile = os.path.join(datadir,roi + '.png')
        # plt.savefig(outfile, format='png')


    	f, ax = plt.subplots()
        y = funcdata[roi]
        old_y = y[old_idx]
        young_y = y[young_idx]
        pib = dvrdata[roi]
        old_pib = pib[old_idx]
        young_pib = pib[young_idx]
        ax.scatter(old_pib, old_y, c='b')
        ax.scatter(young_pib, young_y, c='r')
        (m,b) = polyfit(old_pib, old_y, 1)
        yp = polyval([m,b],old_pib)
        ax.plot(old_pib, yp, 'b-')
        ax.set_xlabel('PIB Index (log)')
        ax.set_ylabel('Functional Connectivity (COPE)')       
        ax.set_title(roi)
        leg = ax.legend(['Old Subjects Best Fit','Old Subjects', 'Young Subjects'],
            loc=0, numpoints=1, scatterpoints=1,prop={'size':10}, markerscale=.8, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        outfile = os.path.join(datadir, roi + '.png')
        plt.savefig(outfile, format='png')
