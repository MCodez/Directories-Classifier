# DIRECTORIES CLASSIFIER

This script will classify the stuff into defined directories and can generate backups for your directory

## HOW DO THE SCRIPT WORK

This script reads the directory (send via arguments on terminal) and classify all the files in defined folders for Images, Word documents, Excel Sheets, Power Point Presentations, Video files, Music files, PDF Files, Text Files, Web Pages (HTML files), Coding files (C/C++/Python/Java), etc..

One can modify the script and increse the sets of extensions for the defined software files. 

This script have two modes for classification:
Mode 0 - In this mode, directories present in the current directory will not be touched and rest other cluttered files will be classified in defined directories.
Mode 1 - In this mode, directories will be read till the leaf file and all the files will be collected. The collected bunch of files and the rest of files will all be classified in defined directories. Finally all the empty directories will be deleted.

This script also provide Backup option (from terminal only). You can backup the directory. It will generate a Zipped Backup File with current Date and Time. This Backup can be unzipped for recovering the files and other sub directories..

## HOW TO INSTALL 

You have to install Python 3.6+ and some libraries listed below.

1. OS
2. SHUTIL
3. RANDOM
4. ZIPFILE
5. DATETIME

All the above mentioned libraries comes with stock Python. In case any library is missing, install it using PIP or WHEEL.

## HOW TO RUN

Open the location of this script in shell/CMD/Terminal and use the following commands.

$ python classifier.py help

This command will display the glimpse of documentation of the script which will include how to run the script.

$ python classifier.py classify pathofdirectory mode

This command will classify the directory at <pathofdirectory> location. Mode will be 0 or 1. Enter the full directory path in double inverted commas.

$ python classifier.py backup pathofdirectory destinationpath

This command will create a Zipped Backup File of directory stored at <pathofdirectory> and store the backup file at <destinationpath>.

## KEY THINGS

If two files with same name encounters, script will handle it automatically by renaming the file name.(Appending will be done)



  


