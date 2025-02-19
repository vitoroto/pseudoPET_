import nibabel as nib
import os
from utils import save_nifti
import cv2
import numpy as np
import SimpleITK as sitk
from MHDtoNIFTI import convert_mhd_to_nifti

pathSlicer = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/Slicer'

pathExtension = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/elastix'
fixed = '/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0018/CT/CT_PETCT_Brain_LM_FDG_STAT_BDD_142747_2.nii.gz'
moving = '/home/vromero2021/Escritorio/TFG/002-DATA/NIFTI/NIFTI_with_FDG_NAC/sub-0018/FLAIR/FLAIR_T2_FLAIR3D_SAG_1.2X1.2X1.2_152032_4.nii.gz'
rigid_parameters = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt'
out_path = '/home/vromero2021/Escritorio/m'

os.system(f'{pathSlicer} --launch {pathExtension} -f {fixed} -m {moving} -p {rigid_parameters} -out {out_path}')


out_out = '/home/vromero2021/Escritorio/r'
pathExtension = '/home/vromero2021/Descargas/Slicer-5.8.0-linux-amd64/slicer.org/Extensions-33216/SlicerElastix/lib/Slicer-5.8/transformix'

os.system(f"{pathSlicer} --launch {pathExtension} -tp '/home/vromero2021/Escritorio/m/TransformParameters.0.txt' -out {out_out} -in {moving}")

for mhd in os.listdir(out_path):
    if mhd.endswith('.mhd'):
        result_mhd = os.path.join(out_path, mhd)

convert_mhd_to_nifti(result_mhd, '/home/vromero2021/Escritorio/result.nii.gz')

