#automate the boring stuff example code 
'''
import os
import shutil

#Get the home directory path as a string
home_dir = os.path.expanduser('~')

#Copying a file to a folder
source1 = os.path.join(home_dir, 'spam', 'file1.txt')
shutil.copy(source1, home_dir)

#Copying a file to a new filename
destination2 = os.path.join(home_dir, 'spam', 'file2.txt')
shutil.copy(source1, destination2)
'''