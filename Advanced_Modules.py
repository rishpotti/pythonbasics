import shutil
import os
import re

#shutil.unpack_archive(r'C:\Users\AppuAchuAnu\Downloads\unzip_me_for_instructions.zip' , r'C:\Users\AppuAchuAnu\Downloads\unzipped_for_instructions', r'zip' )
pattern = r'\d{3}-\d{3}-\d{4}'

for folder, subfolder, file in os.walk(r'C:\Users\AppuAchuAnu\Downloads\unzipped_for_instructions\extracted_content'):
    
    for f in file:
        dir = folder + '\\' + f
        
        x = open(dir)
        text = x.read()
        found = re.search(pattern, text)
        if found != None:
            print(found.group())
            break
            
        x.close()
        

