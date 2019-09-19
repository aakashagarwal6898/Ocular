import os
import shutil
import re


##yourpath = r"E:\Dataset\val_data_tiny"   # target folder with images 
for root, dirs, files in os.walk(yourpath, topdown=False):
    for file_name in files:
         existing_file = re.search("^.*txt$",file_name)
         if existing_file:
            png_file = os.path.splitext(existing_file.group())[0]+".png"
            try:
             shutil.move(os.path.join(r"E:\Dataset\val_data_tiny",png_file),r"E:\Dataset\val_data_DONE_FINAL")
             shutil.move(os.path.join(root,existing_file.group()),r"E:\Dataset\val_data_DONE_FINAL")
            except:
             print("This file does not exists -->"+ png_file)
             continue
