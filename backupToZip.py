#! python3

# 將資料夾備份到ZIP中


import zipfile
import os


def backupToZip(folder):

    #change absloute path
    folder = os.path.abspath(folder)

    number = 1

    #if zipFileName not exists, then break and create one.
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        else:
            number = number + 1


    #Create Zip file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')            



    #Walk entire folder
    for foldername, subfloders, filenames in os.walk(folder):
        print('adding files in %s...' % (foldername))
        #Add current folder to zip
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'

            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            
            backupZip.write(os.path.join(foldername, filename))
            
    backupZip.close()
    
    print('Done.')



backupToZip('C:\\Users\\vend_dt076\\Desktop\\CVD_all')
