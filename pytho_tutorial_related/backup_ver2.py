##
# backup_ver2.py
#
#
# ==================================================
# Written by JuicyITer on Sunday,  9 September 2018.
# For more information, visit https://juicyiter.com
# ==================================================
##
import os
import time

# create backup folder based on date

source = ['~/Desktop/pydir']

target_dir = '/Users/jit/Desktop/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

target = today + os.sep + time.strftime('%H%M%S') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('Successfully done!')
else:
    print('Error encounterd!')

if __name__ == '__main__':
    # testing
    print("Deleting backup files...")
    delete_command = 'rm -r ' + target_dir
    print(delete_command)
    if os.system(delete_command) == 0:
        print("Successful")
    else:
        print("Error")
        
