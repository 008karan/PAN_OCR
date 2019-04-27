from PIL import Image
from PIL import ImageFilter
import utils.logger as logger
#from utils.rotate import rotate
from config import *
from typing import Tuple, List
import sys
i = 0
def crop_image(image, area:Tuple) -> object:
	''' Uses PIL to crop an image, given its area.
	Input:
		image - PIL opened image
		Area - Coordinates in tuple (xmin, ymax, xmax, ymin) format '''
	img1 = Image.open(image)
	img = img1.crop(area)
	basewidth = 200
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	cropped_image = img.resize((basewidth,hsize), Image.ANTIALIAS)
	global i
	cropped_image.save("r" + str(i) + ".jpg", "JPEG",dpi=(300,300))
	i += 1
	
	return cropped_image

def locate_asset(self, image, classifier, lines="") -> List:
	''' Determines where an asset is in the picture, returning
	 a set of coordinates, for the top left, top right, bottom
	 left, and bottom right of the tag
	 Returns:
	 [(area, image)]
	 	Area is the coordinates of the bounding box
	 	Image is the image, opened by PIL.'''
	cropped_images = []
	#print(lines)
	for line in str(lines).split('\n'):
		if "sign" in line:
			continue
		if "photo" in line:
			continue
		#print(line)
		if  "left_x" in line:
			#if 'photo' or 'sign' in line:
			# Extract the nameplate info
			#print(line)
			area = classifier.extract_info(line)
			# Open image
			cropped_images.append((area, crop_image(image, area)))
		
	if cropped_images == []:
		logger.bad("No label found in image.")
	else:
		logger.good("Found " + str(len(cropped_images)) + " label(s) in image.")

	return cropped_images
