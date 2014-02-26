import pandas as pd
import os, sys
import matplotlib.pyplot as plt
import general_stats as gs
import general_plots as gp


if __name__ == '__main__':


    datadir = '/home/jagust/rsfmri_ica/results/DualRegress/ROI/PIB_Index'
    infile = os.path.join(datadir,'ROI_Data.csv')
    design_cols = ['PIB_Index_log','Age_log','Scanner','Motion_log','pve_GM']

    
    data = pd.read_csv(infile, sep='\t')
    olddata = data[data['Group']=='Old']
    youngdata = data[data['Group']=='Young']

    old_x = olddata[design_cols]
    old_x = sm.api.add_constant(old_x, prepend=False)
    young_x = youngdata[design_cols]
    young_x = sm.api.add_constant(young_x, prepend=False)
    for roi in data.columns[7:]:
        # Regress and plot old subject data
        # f, ax = plt.subplots()
        # old_y = olddata[roi]
        # old_rlm_results = gs.run_rlm(old_y, old_x)
        # sm.graphics.regressionplots.plot_ccpr(old_rlm_results, 0, ax=ax)
        # ax.set_xlabel('PIB Index (log)')
        # ax.set_ylabel('Functional Connectivity (COPE)')
        # ax.set_title(roi)
        # # Regress and get mean value for comparison group (young subjects)
        # young_y = youngdata[roi]
        # young_rlm_results = gs.run_rlm(young_y, young_x)
        # young_y_fitted = (young_x['PIB_Index_log'] * young_rlm_results.params['PIB_Index_log'])
        # young_y_part = young_rlm_results.resid + young_y_fitted
        # #young_y_mean = young_y_part.mean()
        # #ax.axhline(y=young_y_mean, color='red', linestyle='--',label='Young Subject Mean Intensity')
        # ax.scatter(young_x['PIB_Index_log'], young_y_part, c='red')
        # leg = ax.legend(['Old Subjects','Old Subjects\nPartial Regression', 'Young Subjects'],
        #     loc=0, numpoints=1, scatterpoints=1,prop={'size':10}, markerscale=.8, fancybox=True)
        # leg.get_frame().set_alpha(0.5)
        # outfile = os.path.join(datadir, roi + '.png')
        # plt.savefig(outfile, format='png')

        f, ax = plt.subplots()
        old_y = olddata[roi]
        young_y = youngdata[roi]
        ax.scatter(old_x.PIB_Index_log, old_y, c='b')
        ax.scatter(young_x.PIB_Index_log, young_y, c='r')
        (m,b) = polyfit(old_x.PIB_Index_log, old_y, 1)
        yp = polyval([m,b],old_x.PIB_Index_log)
        ax.plot(old_x.PIB_Index_log, yp, 'b-')
        ax.set_xlabel('PIB Index (log)')
        ax.set_ylabel('Functional Connectivity (COPE)')       
        ax.set_title(roi)
        leg = ax.legend(['Old Subjects Best Fit','Old Subjects', 'Young Subjects'],
            loc=0, numpoints=1, scatterpoints=1,prop={'size':10}, markerscale=.8, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        outfile = os.path.join(datadir, roi + '.png')
        plt.savefig(outfile, format='png')
