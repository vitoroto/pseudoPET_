import SimpleITK as sitk


def convert_mhd_to_nifti(input_path, output_path):
    # Read the MHD file
    image = sitk.ReadImage(input_path)

    # Write as NIfTI
    sitk.WriteImage(image, output_path)# Example u
