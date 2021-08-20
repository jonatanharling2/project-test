import os
import subprocess
import distutils.dir_util
import glob
import shutil

# Run "make html" in cmd to produce the documentation
subprocess.run('make html', shell=True, check=True)
print('Ran process "make html" in cmd')

# Get the source and destination paths
filepath = os.path.dirname(os.path.realpath(__file__))
source = filepath + '\\_build\\html\\'
destination = os.path.abspath(os.path.join(filepath, '..', 'docs')) + '/'

# Loop through existing files in destination and delete first
print('Deleting existing GitHub pages files')
files = glob.glob(destination + '*')
for f in files:
    if not '_config.yml' in f:
        try:
            os.remove(f)
        except PermissionError:
            # string is probably a folder
            shutil.rmtree(f)

# Copy the content of source to destination
print('Copying contents to GitHub pages docs directory')
distutils.dir_util.copy_tree(source, destination)
print('Process finished')