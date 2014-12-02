import os
from glob import glob
import shutil
import pandas as pd
from nipype.interfaces.base import CommandLine
import nipype.interfaces.utility as util


def make_dir(root, name = 'temp'):
    """ generate dirname string
    check if directory exists
    return exists, dir_string
    """
    outdir = os.path.join(root, name)
    exists = False
    if os.path.isdir(outdir):
        exists = True
    else:
        os.mkdir(outdir)
    return exists, outdir
    

def unzip(infile):
    gunzipfile, gz = os.path.splitext(infile)
    if not 'gz' in gz:
        #when running gunzip on file when
        return infile
    else:
       c3 = CommandLine('gunzip %s'%(infile))
       c3.run()
       return gunzipfile
       
if __name__ == '__main__':

    datadir = '/home/jagust/rsfmri_ica/data'
    bacspet = '/home/jagust/bacs_pet/PIB'
    subinfofile = '/home/jagust/rsfmri_ica/Spreadsheets/Closest_pib_fdg_cog_tofmri_datesonly_10.4.13.csv'
    subinfo = pd.read_csv(subinfofile, sep='\t')

    for subj in subinfo['SUBID']:
        print "Copying data for subject {0}...".format(subj)
           
        sub_pibpath = bacspet
        
        # Determine whether subject is in YOUNG subfolder or not
        if subinfo[subinfo.SUBID==subj]['AGE'].item()=='young':
            sub_pibpath = os.path.join(sub_pibpath, 'young')
        else:
            sub_pibpath = os.path.join(sub_pibpath, 'old')
            #Determine whether subject is in BIOGRAPH folder
        if subinfo[subinfo.SUBID==subj]['SCANNER'].item()=='biograph':
            sub_pibpath = os.path.join(sub_pibpath, 'biograph')
        else:
            sub_pibpath = os.path.join(sub_pibpath, 'ecat')
            
        # Determine which PIB session to grab data from
        if subinfo[subinfo.SUBID==subj]['PIB_SESSION'].item()=='PIB':
            pibsess = '_'.join([subj, 'v1'])
        elif subinfo[subinfo.SUBID==subj]['PIB_SESSION'].item()=='PIB2':
            pibsess = '_'.join([subj, 'v2'])

        subpibdir = os.path.join(sub_pibpath, pibsess, 'pib')
        # Get dvr directory
        globstr = os.path.join(subpibdir, 'dvr*')
        dvrdir = glob(globstr)[0]
        
        # Find dvr image
        globstr = os.path.join(dvrdir, 'DVR*')
        dvrfile = glob(globstr)[0]
        
        # Get coreg directory
        if subinfo[subinfo.SUBID==subj]['SCANNER'].item()=='biograph':
            globstr = os.path.join(subpibdir, 'coreg*')
            coregdir = glob(globstr)[0]
        else:
            globstr = os.path.join(subpibdir, 'realign_QA')
            coregdir = glob(globstr)[0]
            
        #Find mean20min image
        globstr = os.path.join(coregdir, 'mean20min*')
        mean20minfile = glob(globstr)[0]
                
        
        # Make pib directory
        subdatadir = os.path.join(datadir, subj)
        
        exists, newpibdir = make_dir(subdatadir, 'pib')
        
        # Copy dvr file and rename
        shutil.copy(dvrfile, newpibdir)
        unzipped_dvr = unzip(os.path.join(newpibdir, os.path.basename(dvrfile)))
        new_dvr_name = os.path.join(newpibdir, '_'.join([subj, 'dvr.nii']))
        shutil.move(unzipped_dvr, new_dvr_name)
        
        # Copy mean20min file and rename
        shutil.copy(mean20minfile, newpibdir)
        unzipped_mean20min = unzip(os.path.join(newpibdir, os.path.basename(mean20minfile)))
        new_mean20min_name = os.path.join(newpibdir, '_'.join([subj, 'mean20min.nii']))
        shutil.move(unzipped_mean20min, new_mean20min_name)        
        

