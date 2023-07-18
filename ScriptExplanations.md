# File Organizer Python Script

This Python script organizes the files in a directory into specific subdirectories based on their file types. It utilizes Python's `os` and `pathlib` modules.

## How the Script Works

### Importing the Required Modules

The script starts by importing the necessary modules: `os` and `pathlib.Path`. These modules enable the script to interact with the operating system and handle files and directories.

```python
import os
from pathlib import Path
```

### Define the File Categories and Their Extensions
A dictionary called SUBDIRECTORIES is created to map file categories (as keys) to their corresponding file extensions (as values).

```python
SUBDIRECTORIES = {
    'documents': ['.pdf', '.rtf', '.txt'],
    'images': ['.jpg', '.png', '.gif'],
    'audio': ['.mp3', '.wav', '.aiff'],
    'video': ['.mp4', '.mkv', '.flv'],
    #... add more categories and file types as needed
}
```

### Identify the Category of a File
A function named pickDirectory() is defined. It takes a file extension as an argument and determines the file's category by comparing the extension to the ones in SUBDIRECTORIES.

```python
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
```

### Organize Files into Directories
The organizeDirectory() function is defined. This function performs the task of organizing the files.
```python
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
```
In this function:

- It iterates over each item in the current directory, ignoring any items that are directories themselves.
- For each file, it identifies the file type and determines the appropriate directory (category) for this file by calling the `pickDirectory()` function.
- If the directory for this category doesn't exist, it creates a new one.
- Finally, it moves the file into the appropriate directory.


### Start the Organization Process
The organizeDirectory() function is called to kick off the file organization process.

```python
organizeDirectory()
```

## Conclusion
This Python script provides a simple but effective method for file organization. It sorts files based on their types and organizes them into appropriate subdirectories, making your directory structure cleaner and more manageable.
