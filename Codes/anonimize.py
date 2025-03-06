import os
import pydicom

def deidentification(dicomImage):
    ds = pydicom.dcmread(dicomImage)

    ds.InstitutionName = ''
    patientsAge = int(ds.PatientAge[1:3]) + 1600
    date = str(patientsAge) + ds.StudyDate[4:]
    ds.StudyDate = date
    ds.SeriesDate = date
    ds.AcquisitionDate = date
    ds.ContentDate = date
    ds.InstitutionalDepartmentName = ''
    ds.PatientName = ''
    ds.PatientID = ''
    ds.PatientBirthDate = ''
    ds.SourceOfPreviousValues = ''
    ds.ReferringPhysicianName = ''

    ds.save_as(dicomImage)
    print(f"De-identification completed for {dicomImage}.")

def process_dicom_folder(folder_path):

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.dcm'):
                dicom_file = os.path.join(root, file)
                deidentification(dicom_file)

# Replace 'path_to_your_folder' with the actual path to the folder containing DICOM files
folder_path = 'path_to_your_folder'
process_dicom_folder(folder_path)



