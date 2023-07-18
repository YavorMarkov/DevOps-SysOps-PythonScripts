# First, we need some tools: one for dealing with the operating system and one for dealing with file paths
import os
from pathlib import Path

# This is our map. It's like a guide that tells us which kinds of files should go in which folders.
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],  # These are document file types
    "AUDIO":['.m4a','.m4b','.mp3'],  # These are audio file types
    "VIDEOS": ['.mov','.avi','.mp4'],  # These are video file types
    "IMAGES": ['.jpg','.jpeg','.png']  # These are image file types
}

# This helper function helps us decide where a file should go based on its type.
def pickDirectory(value):
    # We look at each category in our map, one by one.
    for category, suffixes in SUBDIRECTORIES.items():
        # For each category, we check each type of file.
        for suffix in suffixes:
            # If the file type matches one in our map, we know which category it belongs to!
            if suffix == value:
                return category
    # If we can't find a match, we say it belongs to the 'MISC' category.
    return 'MISC'

# This function does the heavy lifting. It organizes all the files in a folder.
def organizeDirectory():
    # We look at each item in the folder, one by one.
    for item in os.scandir():
        # If we find a folder, we skip it. We're only interested in files right now.
        if item.is_dir():
            continue
        # We grab some information about the file, like its type.
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        # We decide where this file should go.
        directory = pickDirectory(filetype)
        # We get ready to move the file to that place.
        directoryPath = Path(directory)
        # If the place doesn't exist yet, we create it.
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # Finally, we move the file to the right place.
        filePath.rename(directoryPath.joinpath(filePath))

# We're all set! Let's start cleaning up.
organizeDirectory()

"""This script is like a janitor for your files. 
It goes through your folder, picks up each file, 
looks at its type, and decides where it should go. 
It uses the map we gave it at the beginning to make this decision.
If it can't find the type in the map, it puts the file in a 'MISC' folder. 
If the destination folder doesn't exist yet, it creates one. 
It keeps going until it has sorted all the files in the folder!"""