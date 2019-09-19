import os
import shutil
import re
import multiprocessing



#text_file = open("train.txt","rt")
##
##abc= r"E:\Dataset\images\imagesa\a\a\a\aaa06d00"
for path1 in text_file:
        single_path = re.search("^images.*f",path1)
        shutil.copy(single_path.group(),r"E:\Dataset\train_data")



## uncomment shutil to test and then remove break to copy all the
## files in the folder   

    
                     
