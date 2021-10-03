#!/usr/bin/env python

import hashlib
import os
from shutil import copyfile

# Name of target directory to be sorted
target_dir = "mixed-pics"

def find_duplicates(target_dir):

    # Get absolute path of target directory
    target_path = os.path.join(os.getcwd(), target_dir)

    # Get list of files in target directory
    files_list = os.listdir(target_path)

    # Now check all files are pictures and record any which are not
    pics_list = []
    others_list = []

    for file in files_list:
        
        ext = file[-3:] # grab the file extension
        
        if ext == "jpg" or ext == "png":
            pics_list.append(file)
        else:
            others_list.append(file)

    # Now check for duplicate pictures
    hash_keys = set() # using set because want to quickly check membership
    originals = []
    duplicates = []

    for pic_name in pics_list: # Iterate through picture filenames
        
        pic_path = os.path.join(target_path, pic_name) # Get path of picture
        
        # Generate hash for image
        with open(pic_path, 'rb') as f:
            pic_hash = hashlib.md5(f.read()).hexdigest()

        # If hash not yet encountered add to hash_keys set
        if pic_hash not in hash_keys:
            hash_keys.add(pic_hash)
            originals.append(pic_path)
        # Else add picture path to list of duplicates
        else:
            duplicates.append(pic_path)

    # Print number of files, photos and duplicate photos in target directory
    print(f"""
        There are {len(files_list)} files in the 'mixed-pics' directory.
        {len(pics_list)} of them are pictures and {len(others_list)} are not.
        {len(duplicates)} of the pictures are duplicates.""")

    return duplicates, originals

def copy_originals(originals):
    for pic_path in originals:
        pic_name = os.path.split(pic_path)[-1]
        cp_path = os.path.join(os.getcwd(), "originals", pic_name)
        copyfile(pic_path, cp_path)

def delete_duplicates(duplicates):
    for pic_path in duplicates:
        os.remove(pic_path)

if __name__ == "__main__":
    
    duplicates, originals = find_duplicates(target_dir)
    
    print("""
        Would you like to copy the original files to new folder, or delete the duplicate files in the existing folder?
            \t1) Copy files.
            \t2) Delete files.""")
    
    input_valid = False
    while input_valid == False:
        copy_or_delete = input("\nEnter 1 or 2 (Default 1): ")
        if copy_or_delete == "1" or copy_or_delete == "":
            copy_originals(originals)
            input_valid = True
        elif copy_or_delete == "2":
            delete_duplicates(duplicates)
            input_valid = True
        else:
            print("Input must be either 1 or 2.")
