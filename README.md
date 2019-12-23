# MilkdropPrependFilename
Code by Nathan Williams  
Concept by Jason Fletcher  

### Dependencies
Python 2.7.16 x86  

### Usage
```
python MilkdropPrependFilename.py -v FOLDER_TO_PROCESS
```

### Description
* This python script will copy a filename into memory and then paste it into this same file as a comment into line 1. All other content in the file is pushed down by a single line and no data will be overwritten.
* This is repeated for all files in the given directory with the .milk file extension.
* Files already containing a comment on the first line will be skipped. Any files not matching the .milk extension will be skipped.

### What is this for?
Within the huge collections of user created Milkdrop presets, there are some preset filenames which are extremely long. This is causing problems since the default max file path length in Windows is 256 characters. Yet I wanted to document the original filename so that the original author history is maintained. So while a code comment is not the best solution, in this instance it's the simpliest way given the many thousands of preset files I'm dealing with.

