import zipfile
import shutil


# extract the zipfile
open_zip = zipfile.ZipFile('Project+Day+9.zip','r')
open_zip.extractall()

#can also extract using shutil

'''
shutil.unpack_archive('name', pathName, 'zip')
'''