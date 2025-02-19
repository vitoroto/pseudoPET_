
import nibabel as nib
import os

nifti_dir = '/home/vromero2021/NAS/TFGs/2021_VictorRomero/002-DATA/NIFTI/NIFTI_with_FDG_NAC'

# Recorre los pacientes y modalidades
for patient in os.listdir(nifti_dir):
    patient_path = os.path.join(nifti_dir, patient)
    if os.path.isdir(patient_path):
        for modality in os.listdir(patient_path):
            modality_path = os.path.join(patient_path, modality)
            if os.path.isdir(modality_path):
                for nifti_file in os.listdir(modality_path):
                    if nifti_file.endswith('.nii') or nifti_file.endswith('.nii.gz'):
                        nifti_file_path = os.path.join(modality_path, nifti_file)
                        # Cargar el archivo NIfTI
                        img = nib.load(nifti_file_path)
                        # Obtener las dimensiones
                        dimensions = img.shape
                        print(f'{nifti_file} tiene dimensiones: {dimensions}')
