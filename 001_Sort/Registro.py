"""
002_Registration.py

Rigid registration for paired CT-CBCTs. CT is registered to CBCT (CBCT image spacing and dimensions are maintained).
Registration Matrix is saved and applied to mask.nii.gz (same spacing as CT).

Author: Blanca Rodriguez-Gonzalez (mailto:<blanca.rodriguez@urjc.es>)
Last Edition: 26/11/2024
"""

from utils import load_image
import numpy as np
import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Define input data path
path_in = '/home/blanca/NAS/PROYECTOS_INVESTIGACION/2024-CPT-Simultaneous-Synthesis-Segmentation/002_DATASET/01_OriginalDataset'

# Define where to save bias field corrected dada (does not have to exist)
path_out = '/home/blanca/NAS/PROYECTOS_INVESTIGACION/2024-CPT-Simultaneous-Synthesis-Segmentation/002_DATASET/02_Registered'



# Define your 3D slicer path
path_Slicer = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/Slicer'

path_CT = '/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0002/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_101848_2.nii.gz'
path_MR = '/home/vromero2021/Escritorio/origen.nii.gz'

path_MR_reg = '/home/vromero2021/Escritorio/REG_MR.nii.gz'

img, hdr, aff = load_image(path_MR)
min_MR_val = np.min(img)

os.system(f'{path_Slicer} --launch BRAINSFit --fixedVolume {path_CT} --movingVolume {path_MR} --outputVolume {path_MR_reg}  --transformType Rigid --backgroundFillValue {min_MR_val}')


for subject in os.listdir(path_in):
    print(subject)
    for session in os.listdir(os.path.join(path_in, subject)):
        print(f'\t {session}')

        #create output directory
        create_directory(os.path.join(path_out, subject, session,'REG'))

        # Define in and output CT VOLUMES
        path_CT = os.path.join(path_in, subject, session, 'CT.nii.gz')
        min_CT_val = np.min(load_image(path_CT)[0])
        path_CT_reg = os.path.join(path_out, subject, session, 'CT.nii.gz')

        # Define CBCT in and output volumes
        path_CBCT = os.path.join(path_in, subject, session , 'CBCT.nii.gz')
        path_CBCT_reg = os.path.join(path_out, subject, session, 'CBCT.nii.gz')

        # Define REG matrix
        path_regmatrix = os.path.join(path_out, subject, session, 'REG', 'REG.h5')
        path_regmatrix_mask = os.path.join(path_out, subject, session, 'REG', 'REG_mask.h5')

        # Copy CBCT
        os.system(f'cp {path_CBCT} {path_CBCT_reg}')

        print('\t\t Registering')
        os.system(
            f'{path_Slicer} --launch BRAINSFit --fixedVolume {path_CBCT} --movingVolume {path_CT} --outputVolume {path_CT_reg}  --transformType Rigid --backgroundFillValue {min_CT_val} >/dev/null')



        # Define in and output CT VOLUMES
        path_mask = os.path.join(path_in, subject, session, 'mask.nii.gz')
        path_mask_reg = os.path.join(path_out, subject, session, 'mask.nii.gz')

        os.system(
            f'{path_Slicer} --launch BRAINSFit --fixedVolume {path_CBCT} --movingVolume {path_mask} --outputVolume {path_mask_reg} --outputTransform {path_regmatrix_mask} --transformType Rigid --interpolationMode NearestNeighbor --backgroundFillValue {0} >/dev/null')

        print('\t\t Registration done. \n')