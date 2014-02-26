import nipype.interfaces.freesurfer as fs
from surfer import Brain
import os

def filenames(datadir, ic, hemi, sign):    
    basename = '_'.join(['PIBIndex', sign, '05_05'])
    if sign=='neg':
        basename = '_'.join([basename, 'signed'])
    basename = ''.join([basename, '.nii.gz'])
    infile = os.path.join(datadir, ic, basename)
    outname = ''.join([ic, '_', hemi, '_', sign, '.mgz'])
    outfile = os.path.join(datadir, ic, outname)
    return infile, outfile
    
    
def mri_vol2surf(infile, outfile, hemi, interp='trilinear'):
    sampler = fs.SampleToSurface(hemi=hemi)
    sampler.inputs.source_file = infile
    sampler.inputs.mni152reg=True
    sampler.inputs.sampling_method = "max"
    sampler.inputs.sampling_range = (-3, 2, 0.1)
    sampler.inputs.sampling_units = "mm"
    sampler.inputs.interp_method = interp
    sampler.inputs.out_file = outfile
    sampler.inputs.out_type = 'mgz'
    sampler.inputs.reshape = True
    res = sampler.run()
    return res


def surfer(hemi, overlay, annot='Yeo2011_7Networks_N1000'):
    brain = Brain("fsaverage", hemi, "inflated")
    brain.add_annotation(annot, borders=False, alpha=0.3)
    brain.add_overlay(overlay, min=1.66, max=4)
    return brain

    #brain.show_view({'azimuth': 180, 'elevation': 90})
    

