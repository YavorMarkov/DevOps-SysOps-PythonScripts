import os
from pathlib import Path

# Define a dictionary that maps directory categories to file extensions
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.pgn']
}

# Functions to decide wich directory a file should go into based on its extension
def pickDirectory(value):
    # Loop over all categoruies and file extensions in the directory
    for category, suffixes in SUBDIRECTORIES.items():
        # Check each extension in the current category
        for suffix in suffixes:
            # If the extension matches the one we're looking for, return the category
            if suffix == value:
                return category
    # if no matching extension was found, return 'MISC'
    return 'MISC'

# Function to orginize a directory by moving files into subdirectories based on they extensions
def organizeDirectory():
    # Loop over all items in the current direcotry
    for item in os.scandir():
        # If the item is a direcotry, skip it
        if item.is_dir():
            continue
        # Convert the iutem ti a Path object to get its extension  and other metada
        filePath = Path(item)
        # Gert thhe extension of thhe file
        filetype = filePath.suffix.lower()
        # Decide whichh directory this file should go into
        directory = pickDirectory(filetype)
        # Convert the directory name to a Path object
        directoryPath = Path(directory)
        # If the directory doesn't exist, create it
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # Move the file to hte correct directory
        filePath.rename(directoryPath.joinpath(filePath))

        # Call the function to start organizing the current directory
        organizeDirectory()

