
import os
import numpy 
import pydicom
import numpy as np
from numpy.linalg import norm

filelist=os.listdir('/content/drive/My Drive/DICOM/SE0')

Matrix_size=np.zeros(3)
size_matrix=np.shape(slice_info.pixel_array)
Matrix_size[0]=(size_matrix[0])
Matrix_size[1]=(size_matrix[1])
Matrix_size[2]=(slice_info[0x0021,0x104f].value)
NumEcho=(slice_info[0x0019,0x107e].value)

voxel_size=np.zeros((1,3))
voxel_size[0,0]=slice_info.PixelSpacing[0]
voxel_size[0,1]=slice_info.PixelSpacing[1]
voxel_size[0,2]=slice_info.SpacingBetweenSlices


cf=slice_info.ImagingFrequency
CF=cf*10**6

a_temp=int(Matrix_size[0])
b_temp=int(Matrix_size[1])
c_temp=int(Matrix_size[2]*NumEcho)
isz_real=np.empty((a_temp,b_temp,c_temp))
isz_img=np.empty((a_temp,b_temp,c_temp))

TE=np.empty((NumEcho,1))

r_ImagePositionPatient=np.zeros((3,c_temp))
i_ImagePositionPatient=np.zeros((3,c_temp))
r_EchoNumber=np.zeros((c_temp,1))
i_EchoNumber=np.zeros((c_temp,1))



rctr=0
ictr=0
minSlice=10**10
maxSlice=-1*10**10
progress=''
filelist_length=np.size(filelist)
for i in range (filelist_length):
  fileName=filelist[i]
  slice_info2=pydicom.dcmread(f"{'/content/drive/My Drive/DICOM/SE0/'}{filelist[i]}")
  if slice_info2.SliceLocation < minSlice:
    minSlice=slice_info2.SliceLocation
    minLoc=slice_info2.ImagePositionPatient
  if slice_info2.SliceLocation > maxSlice:
    maxSlice=slice_info2.SliceLocation
    maxLoc=slice_info2.ImagePositionPatient
  if slice_info2.EchoNumbers > NumEcho:
     te=np.zeros((slice_info2.EchoNumbers-NumEcho,1))
     TE=np.array((TE,te))
     NumEcho=slice_info2.EchoNumbers
  if TE[NumEcho-1]==0:
     TE[slice_info2.EchoNumbers]=slice_info2.EchoTime*10**-3
  
  
  if slice_info2.InstanceNumber%3==2:
    rctr=rctr+1
    #for ii in range (np.size(progress)):
      #print('\b')
      #progress=sprintf()
    r_ImagePositionPatient[:,rctr]=slice_info2.ImagePositionPatient
    r_EchoNumber[rctr]=slice_info2.EchoNumbers
    isz_real[:,:,rctr]=abs(slice_info2.pixel_array)
  elif slice_info2.InstanceNumber%3==0:
    ictr=ictr+1
    i_ImagePositionPatient[:,ictr]=slice_info2.ImagePositionPatient
    i_EchoNumber[ictr]=slice_info2.EchoNumbers
    isz_img[:,:,ictr]=abs(slice_info2.pixel_array)
Matrix_size[2]=round(norm((np.subtract(maxLoc,minLoc)),1))+1