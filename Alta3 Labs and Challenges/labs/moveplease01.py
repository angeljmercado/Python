#!/usr/bin/env python3


import shutil   # shell utilities will be used to move files
import os       # provies access to low level os operations

def main():
    """Function to move files to cepth_storage"""
    os.chdir('/home/student/mycode/')   # move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/')  # start moving the file raynor.obj into ceph_storage/ dir

    # Pause and take input
    xname = input('What is the new name for kerrigan.obj? ') # input from user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # Move file with new name


main()



