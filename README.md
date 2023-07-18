# Script Explanation

This README provides a line-by-line explanation of a Python script that organizes files in a directory into specific subdirectories based on their file types.

## Line-By-Line Explanation

```python
import os
```
This line imports the os module in Python, which provides functions for interacting with the operating system. This module allows us to use OS dependent functionalities like reading or writing to the file system.

```
from pathlib import Path
```
The pathlib module in Python provides various classes representing filesystem paths with semantics appropriate for different operating systems. The Path class is specifically used for manipulating file paths.

```
SUBDIRECTORIES = {...}
```
Here, we define a dictionary named SUBDIRECTORIES which maps categories of file types (as keys) to corresponding file extensions (as values).

```
def pickDirectory(value):

```

A function pickDirectory is defined which takes a file extension as an argument.
```
for category, suffixes in SUBDIRECTORIES.items():
    for suffix in suffixes:
        if suffix == value:
            return category
```
These lines loop through all the file extensions in our dictionary SUBDIRECTORIES. If the provided file extension matches any of the dictionary's extensions, the function returns the corresponding category.

```
return 'MISC'
```
If the provided file extension does not exist in the SUBDIRECTORIES dictionary, the function returns 'MISC'.

```
def organizeDirectory():
```

The organizeDirectory function is defined. This function does the main task of sorting the files.

```
for item in os.scandir():
```
This line iterates over all files and directories in the current directory.

```
if item.is_dir(): continue
```
If the item is a directory, it skips the current iteration and continues with the next item.

```
filePath = Path(item)
```
This line creates a Path object of the item, which represents the file path.

```
filetype = filePath.suffix.lower()
```
This line gets the extension of the file and converts it to lowercase.

```
directory = pickDirectory(filetype)
```
This line calls the pickDirectory function with the file extension as the argument. This determines the category of the file.

```
directoryPath = Path(directory)
```
This line creates a Path object for the determined directory.

```
if directoryPath.is_dir() != True: directoryPath.mkdir()
```
This line checks if the directory exists. If not, it creates the directory.

```
filePath.rename(directoryPath.joinpath(filePath))
```
This line moves the file to the appropriate directory.

```
organizeDirectory()
```
Finally, this line calls the organizeDirectory function to start the process.


#####In summary, this script is used to sort files in the current directory into their respective subdirectories based on their file types.


