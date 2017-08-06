# Rename files in a directory

Lists all files in a specified directory `[source_directory]` . Separates the file extension from the file name`[file_extension]` . If the file extensions are not includes in the exclusion list, then renames the files with the original file extension into another specified directory `[destination_directory]` . The new file name is based on enumerator `[my_enumerator]` , formated date `[day_formated]` , time `[time_formated]` and original file extension `[file_extension]`

### To use this scrip
1. Edit **source_directory** variable with your own directory path where the files you wish
to be renamed are located.
```
source_directory = "your Source Directory Path"
```

2. Edit **destination_directory** variable with your own directory path where the renamed files will be saved.
```
destination_directory = "your Destination Directory Path"
```

3. If you would like to modify the **exclusion** file list edit the extensions after `!=` :
 ```
 if file_extension != '.ini' and '.txt'
 ```

4. Run the script

### Notes
If you would like to turn the **"exclude"** list into an **"include"** list, change `!=` to `==`:
```
if file_extension == '.doc' and '.pdf'
```
This will **only** rename/move files ending in '.doc' and '.pdf' in the **source_directory**


:shipit: