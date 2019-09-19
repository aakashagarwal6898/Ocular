#new_text = open(filename+".txt","w") 	

#def yolo_ann(class_index,bounds,image,new_text):
    width, height = image.size

    for bound in bounds:
                
      xmin=bound.vertices[0].x
      ymin=bound.vertices[0].y
      xmax=bound.vertices[2].x 
      ymax=bound.vertices[2].y

      xcen = float((xmin + xmax)) / 2 / width   	##self.imgSize[1]	#width =[1]
      ycen = float((ymin + ymax)) / 2 / height  	##self.imgSize[0]       #height=[0]

      w = float((xmax - xmin)) / width   		##self.imgSize[1]
      h = float((ymax - ymin)) / height  		##self.imgSize[0]

      new_text.write("%d %.6f %.6f %.6f %.6f\n" % (class_index, xcen, ycen, w, h))






-Take inputs [top-left(xmin,ymin) & bottom-right(xmax,ymax)] and [height & width of image]
 and [class_index].

-convert them into xcen,ycen,width,height.

-write class_index xcen ycen width height in .txt format.
