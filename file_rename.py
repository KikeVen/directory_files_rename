# python file_rename.py

import os
import datetime

# "C:\\Users\\user\\(YorDirectoryPath)\\"
source_directory = "your Source Directory Path"
destination_directory = "your Destination Directory Path"

date_time = datetime.datetime.now()
date = date_time.date()  # gives date
time = date_time.time()  # gives time

time_formated = datetime.datetime.strptime(str(time), "%H:%M:%S.%f")
time_formated = time_formated.strftime("%S%f%p")

day_formated = datetime.datetime.strptime(str(date), "%Y-%m-%d")
day_formated = day_formated.strftime("%m%d%Y")


def file_rename():
    """
    Lists all files in a specified directory (source_directory). Separates the file extension
    from the file name (file_extension). If the file extensions are not includes in the exclusion 
    list, then renames the files with the original file extension into another specified 
    directory (destination_directory) with a new name based on enumerator (my_enumerator), 
    formated date (day_formated), time (time_formated) and original file extension (file_extension)
    """

    my_enumerator = 1
    for file in os.scandir(source_directory):
        if file.is_file():
            file_extension = os.path.splitext(file.name)[1]
            if file_extension != '.ini' and '.txt':
                print(str(my_enumerator) + time_formated +
                      day_formated + file_extension)
                os.rename(os.path.join(source_directory, file.name), os.path.join(
                    destination_directory, str(my_enumerator) + time_formated + day_formated + file_extension))
            my_enumerator += 1

if __name__ == "__main__":
    file_rename()
