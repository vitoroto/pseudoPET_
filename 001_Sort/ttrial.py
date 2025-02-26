import nibabel as nib
import os
from utils import save_nifti
import cv2
import numpy as np
import SimpleITK as sitk
from MHDtoNIFTI import convert_mhd_to_nifti
import shutil

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

pathSlicer = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/Slicer'
pathExtension = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/elastix'
temp_intermideate = '/home/vromero2021/Escritorio/m'
rigid_parameters = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/qt-scripted-modules/Resources/RegistrationParameters/Rigid.txt'
temporal_result = '/home/vromero2021/Escritorio/r'
pathExtension_transformix = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/transformix'




input = '/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC'
output = '/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI_REGISTERED/NIFTI_with_FDG_NAC'
for patient in os.listdir(input):
    create_dir(os.path.join(output, patient))
    for modality in os.listdir(os.path.join(input, patient)):
        if modality == 'CT':
            create_dir(os.path.join(output, patient, modality))
            for volume in os.listdir(os.path.join(input, patient, modality)):
                if volume.endswith('.nii.gz'):
                    fixed_CT = os.path.join(input, patient, modality, volume) # /home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0001/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_130108_2.nii.gz
                    shutil.copy(fixed_CT, os.path.join(output, patient, modality, volume))

        if modality == 'FDG':
            create_dir(os.path.join(output, patient, modality))
            for volume in os.listdir(os.path.join(input, patient, modality)):
                if volume.endswith('.nii.gz'):
                    fixed_FDG = os.path.join(input, patient, modality, volume) # /home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0001/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_130108_2.nii.gz
                    shutil.copy(fixed_FDG, os.path.join(output, patient, modality, volume))

        elif modality == 'FDG_NAC':
            create_dir(os.path.join(output, patient, modality))
            for volume in os.listdir(os.path.join(input, patient, modality)):
                if volume.endswith('.nii.gz'):
                    fixed_FDG_NAC = os.path.join(input, patient, modality, volume) # /home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0001/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_130108_2.nii.gz
                    shutil.copy(fixed_FDG_NAC, os.path.join(output, patient, modality, volume))

        elif modality == 'FLAIR':
            create_dir(os.path.join(output, patient, modality))
            for volume in os.listdir(os.path.join(input, patient, modality)):
                if volume.endswith('.nii.gz'):
                    moving_FLAIR = os.path.join(input, patient, modality, volume)  # /home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0001/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_130108_2.nii.gz
                    os.system(
                        f'{pathSlicer} --launch {pathExtension} -f {fixed_CT} -m {moving_FLAIR} -p {rigid_parameters} -out {temp_intermideate}')
                    os.system(
                        f"{pathSlicer} --launch {pathExtension_transformix} -tp '{temp_intermideate}/TransformParameters.0.txt' -out {temporal_result} -in {moving_FLAIR}")
                    for mhd in os.listdir(temporal_result):
                        if mhd.endswith('.mhd'):
                            result_mhd = os.path.join(temporal_result, mhd)
                        convert_mhd_to_nifti(result_mhd, f'/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI_REGISTERED/NIFTI_with_FDG_NAC/{patient}/{modality}/Registered_FLAIR.nii.gz')
                    os.system(f'rm -rf {temp_intermideate}/*')
                    os.system(f'rm -rf {temporal_result}/*')
                    print('saved')
        elif modality == 'T1':
            create_dir(os.path.join(output, patient, modality))
            for volume in os.listdir(os.path.join(input, patient, modality)):
                if volume.endswith('.nii.gz'):
                    moving_T1 = os.path.join(input, patient, modality, volume)  # /home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0001/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_130108_2.nii.gz
                    os.system(
                        f'{pathSlicer} --launch {pathExtension} -f {fixed_CT} -m {moving_T1} -p {rigid_parameters} -out {temp_intermideate}')
                    os.system(
                        f"{pathSlicer} --launch {pathExtension_transformix} -tp '{temp_intermideate}/TransformParameters.0.txt' -out {temporal_result} -in {moving_T1}")
                    for mhd in os.listdir(temporal_result):
                        if mhd.endswith('.mhd'):
                            result_mhd = os.path.join(temporal_result, mhd)
                    convert_mhd_to_nifti(result_mhd, f'/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI_REGISTERED/NIFTI_with_FDG_NAC/{patient}/{modality}/Registered_T1.nii.gz')
                    os.system(f'rm -rf {temp_intermideate}/*')
                    os.system(f'rm -rf {temporal_result}/*')

import pydicom as pdcm
import numpy as np

pet_path = '/home/javier/NAS/TFGs/2021_VictorRomero/002-DATA/001-DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata/sub-0002/FDG/PT-0005-0002.dcm'

pet = pdcm.dcmread(pet_path)

print(pet)