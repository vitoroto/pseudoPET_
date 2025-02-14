import os
import shutil


os.chdir('/home/vromero2021/NAS/TFGs/2021_VictorRomero/002-DATA')

for patient in os.listdir('.//DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata'):
    for modality in os.listdir(f'.//DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata/{patient}'):
        print(f'Processing {modality} for patient {patient}...')
        if not os.path.exists(f'.//NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality}'):
            os.makedirs(f'.//NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality}')
            os.system(f'dcm2niix -o /home/vromero2021/NAS/TFGs/2021_VictorRomero/002-DATA/NIFTI/NIFTI_with_FDG_NAC/{patient}/{modality} -z y -b y /home/vromero2021/NAS/TFGs/2021_VictorRomero/002-DATA/DCM_ORIGINAL/DICOM_with_FDG_NAC/sourcedata/{patient}/{modality}')
            print(f'Done {modality} for patient {patient}\n')
