'''' Reading Multi-Echo GRE sequence in to Magnitude, Real and Imaginary files in Instack Position'''
import os
import numpy 
import pydicom
import numpy as np
from numpy.linalg import norm

# Reding single file list in the dicom folder
# Read any of the file in dicomfolder to get Matrix Size, Voxel Size, Number of slices and Number of Echoes 
filelist=os.listdir('D:\FARSANA\DataSets\DICOM\SE0')
slice_info=pydicom.dcmread('/content/drive/My Drive/DICOM/SE0/IM0')
#Matrix Size from dicom tag
Matrix_size=np.zeros(3)
size_matrix=np.shape(slice_info.pixel_array)
Matrix_size[0]=(size_matrix[0])
Matrix_size[1]=(size_matrix[1])
Matrix_size[2]=(slice_info[0x0021,0x104f].value)
#Number of Echo from dicom tag
NumEcho=(slice_info[0x0019,0x107e].value)
# voxel size from dicom
voxel_size=np.zeros((1,3))
voxel_size[0,0]=slice_info.PixelSpacing[0]
voxel_size[0,1]=slice_info.PixelSpacing[1]
voxel_size[0,2]=voxel_size[0,2]=int(slice_info.SpacingBetweenSlices)
# Centre Frequency
cf=slice_info.ImagingFrequency
CF=cf*10**6
#---------------------------------------------------------
a_temp=int(Matrix_size[0])
b_temp=int(Matrix_size[1])
instack_position=int(Matrix_size[2])

## magnitude components to in-stack posittion
rs1=0 # variable assigned for slice location for first echo
rs2=0 # variable assigned for slice location for second echo
rs3=0 # variable assigned for slice location for Third echo
rs4=0 # variable assigned for slice location for fourth  echo
rs5=0 #variable assigned for slice location for ffth echo
rsz_E1=np.empty((a_temp,b_temp,instack_position)) # first_Echo
rsz_E2=np.empty((a_temp,b_temp,instack_position)) #Second_Echo
rsz_E3=np.empty((a_temp,b_temp,instack_position)) # Third_Echo
rsz_E4=np.empty((a_temp,b_temp,instack_position)) # Fourth_Echo
rsz_E5=np.empty((a_temp,b_temp,instack_position)) #Fifth_Echo
filelist=os.listdir('/content/drive/My Drive/DICOM/SE0')
filelist_length=np.size(filelist)
for i in range(filelist_length):
  slice_info1=pydicom.dcmread(f"{'/content/drive/My Drive/DICOM/SE0/'}{filelist[i]}")
  if slice_info1[0x0043,0x102f].value==0:
    for j in range(2,69):
      if slice_info1.InStackPositionNumber==j+1:
        if slice_info1.EchoNumbers==1:
          rs1=rs1+1
          rsz_E1[:,:,rs1]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==2:
          rs2=rs2+1
          rsz_E2[:,:,rs2]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==3:
          rs3=rs3+1
          rsz_E3[:,:,rs3]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==4:
          rs4=rs4+1
          rsz_E4[:,:,rs4]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==5:
          rs5=rs5+1
          rsz_E5[:,:,rs5]=slice_info1.pixel_array
  break


## Imaginary components to in-stack posittion
Is1=0
Is2=0
Is3=0
Is4=0 
Is5=0
Isz_E1=np.empty((a_temp,b_temp,instack_position))
Isz_E2=np.empty((a_temp,b_temp,instack_position))
Isz_E3=np.empty((a_temp,b_temp,instack_position))
Isz_E4=np.empty((a_temp,b_temp,instack_position))
Isz_E5=np.empty((a_temp,b_temp,instack_position))
filelist=os.listdir('/content/drive/My Drive/DICOM/SE0')
filelist_length=np.size(filelist)
for i in range(filelist_length):
  slice_info1=pydicom.dcmread(f"{'/content/drive/My Drive/DICOM/SE0/'}{filelist[i]}")
  if slice_info1[0x0043,0x102f].value==2:
    for j in range(2,69):
      if slice_info1.InStackPositionNumber==j+1:
        if slice_info1.EchoNumbers==1:
          Is1=Is1+1
          Isz_E1[:,:,Is1]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==2:
          Is2=Is2+1
          Isz_E2[:,:,Is2]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==3:
          Is3=Is3+1
          Isz_E3[:,:,Is3]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==4:
          Is4=Is4+1
          Isz_E4[:,:,Is4]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==5:
          Is5=Is5+1
          Isz_E5[:,:,Is5]=slice_info1.pixel_array
  break

## phase components to in-stack posittion
ps1=0
ps2=0
ps3=0
ps4=0 
ps5=0
psz_E1=np.empty((a_temp,b_temp,instack_position))
psz_E2=np.empty((a_temp,b_temp,instack_position))
psz_E3=np.empty((a_temp,b_temp,instack_position))
psz_E4=np.empty((a_temp,b_temp,instack_position))
psz_E5=np.empty((a_temp,b_temp,instack_position))
filelist=os.listdir('/content/drive/My Drive/DICOM/SE0')
filelist_length=np.size(filelist)
for i in range(filelist_length):
  slice_info1=pydicom.dcmread(f"{'/content/drive/My Drive/DICOM/SE0/'}{filelist[i]}")
  if slice_info1[0x0043,0x102f].value==2:
    for j in range(2,69):
      if slice_info1.InStackPositionNumber==j+1:
        if slice_info1.EchoNumbers==1:
          ps1=ps1+1
          psz_E1[:,:,ps1]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==2:
          ps2=ps2+1
          psz_E2[:,:,ps2]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==3:
          ps3=ps3+1
          psz_E3[:,:,ps3]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==4:
          ps4=ps4+1
          psz_E4[:,:,ps4]=slice_info1.pixel_array
        elif slice_info1.EchoNumbers==5:
          ps5=ps5+1
          psz_E5[:,:,ps5]=slice_info1.pixel_array
  break        