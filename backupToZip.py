#! python3

# 將資料夾備份到ZIP中


import zipfile
import os

def backupToZip(floder):

    folder = os.path.abspath(folder)

    number = 1
    
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        else:
            number = number + 1


    #TODO: Create Zip file

    #TODO: Walk entire folder

    print('Done.')


            
