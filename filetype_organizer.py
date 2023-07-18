# Importing required modules
import os
from pathlib import Path

# A dictionary to map file types with their respective categories
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# Function to determine the category of a given file type
def pickDirectory(value):
    # Iterate over all items in the SUBDIRECTORIES dictionary
    for category, suffixes in SUBDIRECTORIES.items():
        # For each category, iterate over the file types
        for suffix in suffixes:
            # If the file type matches with the given value, return the category
            if suffix == value:
                return category
    # If the file type is not found in the dictionary, return 'MISC'
    return 'MISC'

# Function to organize files into respective directories based on their category
def organizeDirectory():
    # Iterate over all items in the current directory
    for item in os.scandir():
        # If the item is a directory, skip and continue with the next item
        if item.is_dir():
            continue
        # Get the path of the current item
        filePath = Path(item)
        # Get the file type (extension) of the current file and convert it to lowercase
        filetype = filePath.suffix.lower()
        # Get the category of the current file type
        directory = pickDirectory(filetype)
        # Get the path of the directory where the current file should be moved
        directoryPath = Path(directory)
        # If the directory does not exist, create it
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # Move the current file to the respective directory
        filePath.rename(directoryPath.joinpath(filePath))

# Call the function to start organizing the directory
organizeDirectory()
