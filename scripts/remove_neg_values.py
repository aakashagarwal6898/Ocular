import os

yourpath = r"E:\Dataset\Dataset_tiny_final\text_files"   # target folder with images 
for root, dirs, files in os.walk(yourpath, topdown=False):
    for filename in files:

        txt_file = open(os.path.join(root,filename),"r")
        new_txt = open(filename,"w")
        for txt_line in txt_file:
            txt_line=txt_line.replace("-","")
            new_txt.write(txt_line)
        txt_file.close()
        new_txt.close()
        break
            
