# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 08:41:53 2018

@author: tony3
"""
# STUFF I WANNA USE 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg 
from skimage.filters import threshold_minimum
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.segmentation import clear_border

plt.close('all')  #close all open plots, start fresh

####    YOU MUST CHANGE THE PATH STRING BELOW TO LOAD YOUR BEAD PHOTO     ####
#########################################################################
I = mpimg.imread("testa.jpg")  #load the image
##########################################################################

Ir = I.copy() #red channel
Ir[:,:,1]=0  #Image files are 3 D matrix where  0 = red, 1 = green, 2 = blue
Ir[:,:,2]=0
Ig = I.copy() #green channel, really all we need but want to show you diff
Ig[:,:,0]=0 # set reds to zero
Ig[:,:,2]=0 # set blues to zero
Ib = I.copy()  #blue channel
Ib[:,:,0]=0
Ib[:,:,1]=0

f, ax = plt.subplots(2, 2) #create a 2 x 2 set of subplots (4 total)
ax[0,0].set_title('Raw Img') #set the figure title
ax[0,0].imshow(I)  #show the image
ax[0,0].axis('off') #images need no axis
ax[0,1].set_title('Red Channel') #set the title for red
ax[0,1].imshow(Ir)
ax[0,1].axis('off')
ax[1,0].set_title('Green Channel') #set the title for green
ax[1,0].imshow(Ig)
ax[1,0].axis('off')
ax[1,1].set_title('Blue Channel') #set the title for blue
ax[1,1].imshow(Ib)
ax[1,1].axis('off')

Igg=I.copy() #goind to make BW img out of green channel
Igg[:,:,0]=Igg[:,:,1]  #red and blue get same values as green channel
Igg[:,:,2]=Igg[:,:,1]
f, ax = plt.subplots(2, 2) # make another 2x2 plot
ax[0,0].imshow(Igg)  #show gray scale image of green channel
ax[0,0].axis('off')
ax[0,0].set_title('Green Channel, BW')

#### YOU MIGHT NEED TO CHANGE THE THRESHOLD BELOW TO PICK OUT FROM NOISE   ####
#### AND IGNORE SHADOWS. HIGHER VALUES MEANS MORE GRAYS WILL BE MADE BLACK ####
#############################################################################
thresh=160;  #cutoff between B & W
#Just FYI, threshold_minimum would be a good bit of code to use here
#you can read what threshold_minimum(Igg[:,:,2]) does here:
#     http://scikit-image.org/docs/dev/api/skimage.filters.html 
#############################################################################

ax[0,1].hist(Igg.ravel(), bins=256, log=True) #log histogram, pixel brightness
ax[0, 1].axvline(thresh, color='r')  #draw a vertical line at threshold
IBinary = (Igg[:,:,2] > thresh) #array where true at brightness > threshold
ax[1,0].imshow(IBinary, cmap=plt.cm.gray) # show new BW image with BW colormap

# The follwoing dialates and erodes toget rid of specks
# If your beads are too speckled, you may want to play with the square there
# Then converts blacks to whites and removes border objects 
IBinaryFix = clear_border(1- closing(IBinary,square(3)))

ax[1,1].imshow(IBinaryFix, cmap=plt.cm.gray)   #show it...

label_image = label(IBinaryFix)# find and lable all white contiguous shapes
image_label_overlay = label2rgb(label_image, I, alpha=.3) #combine with original img
f, ax = plt.subplots(1, 1) #new plot
ax.imshow(image_label_overlay)  #plot the overlay image

region_properties = regionprops(label_image, coordinates='xy')#get properties of labeled regions
#For all the properties you can assess see: 
#         http://scikit-image.org/docs/dev/api/skimage.measure.html
n = len(region_properties) #number of objects detected
d=np.zeros(n) #container for our diameters
e=np.zeros(n) #container for our eccentricities
i=0  # a counter
for region in region_properties:  #loop through all the discovered objects
    # take regions with large enough areas
    ###########   Only take larger obejects (remove specs)
    ###########   Depending on the resolution of your camera
    ###########   you may need to change this min size on next line
    if region.area >= 100:  
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox  #object's bounding box
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='white', linewidth=1)
        ax.add_patch(rect)   #outline object with rectangle
        d[i]=(maxc - minc + maxr - minr)/2  #diameter is avg of width & height
        e[i]= region.eccentricity  #closer to 0 is closer to circle
        i+=1  #advance counter
ax.set_axis_off()


"""From here you need to get rid of zeros, convert diameters in pixel into mm, and create
a histogram of diameters and eccentricities for your beads. Get means and 
stdevs too."""