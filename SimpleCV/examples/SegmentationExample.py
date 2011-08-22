#!/usr/bin/python
#
import time
import pdb
from SimpleCV import *
from SimpleCV.Display import Display, pg

display = Display(resolution = (800, 600)) #create a new display to draw images on
cam = Camera() #initialize the camera
done = False # setup boolean to stop the program

count = 0 
#segmentor = ColorSegmentation()
segmentor = CodebookSegmentation();
# Loop until not needed

temp = cam.getImage()
#segmentor.addToModel(temp)

while not display.isDone():
    image = cam.getImage()
    blobLayer = DrawingLayer((image.width,image.height))    
    segmentor.addImage(image)
        
    if(segmentor.isReady()):
        test = segmentor.getRawImage()
        blobs = segmentor.getSegmentedBlobs()
        
        for b in blobs:
            b.draw(color=Color.RED,layer=blobLayer,alpha=128)

    image.addDrawingLayer(blobLayer)
    image.save(display)
    image.clearLayers()
    time.sleep(0.01) # Let the program sleep for 1 millisecond so the computer can do other things
    if display.mouseLeft:
        display.done = True #if the left arrow is pressed, close the program