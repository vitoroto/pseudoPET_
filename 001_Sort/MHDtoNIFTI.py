import SimpleITK as sitk


def convert_mhd_to_nifti(input_path, output_path):
    # Read the MHD file
    image = sitk.ReadImage(input_path)

    # Write as NIfTI
    sitk.WriteImage(image, output_path)


# Example usage
convert_mhd_to_nifti("/home/vromero2021/Escritorio/r/result.mhd", "/home/vromero2021/Escritorio/r/result.nii.gz")

