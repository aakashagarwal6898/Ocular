import os
from PIL import Image

##yourpath = r"E:\Dataset\aa_test_src"   # target folder with images 
##for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files: 
                tif_file = os.path.splitext(os.path.join(r"E:\Dataset\aa_test_dest", name))[0] + ".png"
                try:
                 im = Image.open(os.path.join(root, name))
                 im.thumbnail(im.size)
                 im.save(tif_file, "PNG", quality=100)
                except:
                 print("delete these from E:\Dataset\sample_test --> \n",os.path.join(root, name))
                 continue
                




