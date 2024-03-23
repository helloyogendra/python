import os
import shutil
import re

source = r"C:\temp\source"
dest = r"C:\temp\source\arch"
patt = "20230707"

def move_files_to_archive_by_pattern(source_folder, archival_folder, pattern):
    
    for item_name in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item_name)

        if os.path.isfile(item_path):
            if item_name.startswith(pattern):
                
                archival_path = os.path.join(archival_folder, item_name)
                shutil.move(item_path, archival_path)
                print(f"Moved file to archive: {item_name}")



move_files_to_archive_by_pattern(source, dest, patt)
