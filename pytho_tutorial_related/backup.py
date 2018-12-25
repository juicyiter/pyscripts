##
# backup.py
#
#
# =================================================
# Written by JuicyITer on Sunday,  9 September 2018.
# For more information, visit https://juicyiter.com
# =================================================
##
import os
import time

# Files to be backuped are stored in a list

source = ['C:\\Users\\JuicyITer\\Desktop\\notes', \
          'C:\\Users\\JuicyITer\\Desktop\\pydir']
# Example on the Unix-like OS
# source = ['/Users/JuicyITer/Desktop/notes']

# files are stored at target_dir
target_dir = 'C:\\Users\\JuicyITer\\Desktop\\backup'

# files are backuped into a zip file
# The name of the zip file is the current date and time

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%C%S') + \
         '.zip'

# Create the target directory if it's not present

if not os.path.exists(target_dir):
    os.mkdir(target_dir)        # make dir

# Use the zip command to put the files in a zip
zip_command = 'zip -r {0} {1}'.format(target, join(source))

# run the backup
print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    # successful
    print('Successfully backup to', target)
else:
    print('Backup FAILED')
