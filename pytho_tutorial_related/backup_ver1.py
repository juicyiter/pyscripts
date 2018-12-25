##
# backup.py
#
#
# =================================================
# Written by JuicyITer on Sunday,  9 September 2018.
# For more information, visit https://juicyiter.com
# =================================================
##
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
# example on the windows
# source = ['C:\\Users\\JuicyITer\\Desktop\\notes'] 
# or using raw string [r'C:\Users..."]
source = ['~/Desktop/CS-Notes', '~/Desktop/pydir']

# files are stored at target_dir
target_dir = '/Users/jit/Desktop/backup'

# files are backuped into a zip file
# The name of the zip file is the current date and time

# os.sep gives the directory separator -> / or "\\"

# time.strftime generates the current time with
# the format blah blah
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%C%S') + \
         '.zip'

# Create the target directory if it's not present

if not os.path.exists(target_dir):
    os.mkdir(target_dir)        # make dir

# Use the zip command to put the files in a zip

# ' '.join(source) joins the ' ' and the source (list) into a string
# where ' ' seperates each item

# -r option specifies zip should work recursively for directories
# which means it should include all the subdirectories and files
# Options are followd by the targe zip archive to create
# followed by the list of files and directories to be backuped
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


# run the backup
print('Zip command is:')
print(zip_command)
print('Running:')

# os.system runs the command as if it was run from the system i.e.
# in the shell. It should return 0 if the command was successful,
# else it returns an error number
if os.system(zip_command) == 0:
    # successful
    print('Successfully backup to', target)
else:
    print('Backup FAILED')
