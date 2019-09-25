import os
import argparse
from enum import Enum
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import shutil  


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="E:\Dataset\My First Project-7b06713586f3.json"

class FeatureType(Enum):
    
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5
    NULL_V=6
    
def get_document_bounds(image_file, feature1, feature2,feature3,feature4,feature5):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []
    bounds_BLOCK = []
    bounds_PARA = []
    bounds_WORD = []
    

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature5 == FeatureType.SYMBOL):
                            bounds.append(symbol.bounding_box)

                    if (feature4 == FeatureType.WORD):
                        bounds_WORD.append(word.bounding_box)

                if (feature3 == FeatureType.PARA):
                    bounds_PARA.append(paragraph.bounding_box)

            if (feature2 == FeatureType.BLOCK):
                bounds_BLOCK.append(block.bounding_box)

        if (feature1 == FeatureType.PAGE):
            bounds.append(block.bounding_box)

    # The list `bounds` contains the coordinates of the bounding boxes.
    return bounds_BLOCK,bounds_PARA,bounds_WORD

def yolo_ann(class_index,bounds,image,new_text):
    width, height = image.size

    for bound in bounds:
                
      xmin=bound.vertices[0].x
      ymin=bound.vertices[0].y
      xmax=bound.vertices[2].x 
      ymax=bound.vertices[2].y

      xcen = float((xmin + xmax)) / 2 / width   	
      ycen = float((ymin + ymax)) / 2 / height  	

      w = float((xmax - xmin)) / width   		
      h = float((ymax - ymin)) / height  		

      new_text.write("%d %.6f %.6f %.6f %.6f\n" % (class_index, xcen, ycen, w, h))

def render_doc_text(filein):
  image = Image.open(filein)
  new_text = open(filein.strip(".png")+".txt","w")
  
  
  
  bounds_BLOCK,bounds_PARA,bounds_WORD = get_document_bounds(filein, FeatureType.NULL_V, FeatureType.BLOCK, FeatureType.PARA, FeatureType.WORD, FeatureType.NULL_V)
  
  yolo_ann(0,bounds_BLOCK,image,new_text)
  
  yolo_ann(1,bounds_PARA,image,new_text)
  
  yolo_ann(2,bounds_WORD,image,new_text)
  
  new_text.close()
   


  


if __name__ == '__main__':

    yourpath = r"E:\Dataset\train_data_tiny"   # target folder with images 
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files:
##            try:
              render_doc_text(name)
##             shutil.move(name.strip(".png")+".txt",r"E:\Dataset\val_data_LABELS")

##            except:
##             print("FIX THIS-->",os.path.join(root, name))
##             continue


















        
