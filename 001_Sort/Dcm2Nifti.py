import os
import shutil
import dicom2nifti

os.chdir('/home/vromero2021/Escritorio/TFG/002-DATA')

for patient in os.listdir('.//DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata'):
    for modality in os.listdir(f'.//DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata/{patient}'):
        print(f'Processing {modality} for patient {patient}\n')
        if not os.path.exists(f'.//NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality}'):
            os.makedirs(f'.//NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality}')
            dicom2nifti.convert_dir.convert_directory(f'./DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata/{patient}/{modality}',
            f'./NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality}', compression=True, reorient=True)
            print(f'Done {modality} for patient {patient}\n')
