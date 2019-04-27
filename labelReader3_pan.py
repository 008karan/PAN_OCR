#!/bin/bash
from __future__ import print_function
from config import *
from utils.darknet_classify_image import *
from utils.tesseract_ocr import *
import utils.logger as logger
import sys
from PIL import Image
import time
import os
import re
from operator import itemgetter
PYTHON_VERSION = sys.version_info[0]
OS_VERSION = os.name
import pandas as pd

class PanOCR():
	''' Finds and determines if given image contains required text and where it is. '''

	def init_vars(self):
		try:
			self.DARKNET = DARKNET
			
			self.TESSERACT = TESSERACT
			

			return 0
		except:
			return -1

	def init_classifier(self):
		''' Initializes the classifier '''
		try:
			if self.DARKNET:
			# Get a child process for speed considerations
				logger.good("Initializing Darknet")
				self.classifier = DarknetClassifier()
			
			if self.classifier == None or self.classifier == -1:
				return -1
			return 0
		except:
			return -1

	def init_ocr(self):
		''' Initializes the OCR engine '''
		try:
			if self.TESSERACT:
				logger.good("Initializing Tesseract")
				self.OCR = TesseractOCR()
			
			if self.OCR == None or self.OCR == -1:
				return -1
			return 0
		except:
			return -1

	def init_tabComplete(self):
		''' Initializes the tab completer '''
		try:
			if OS_VERSION == "posix":
				global tabCompleter
				global readline
				from utils.PythonCompleter import tabCompleter
				import readline
				comp = tabCompleter()
				# we want to treat '/' as part of a word, so override the delimiters
				readline.set_completer_delims(' \t\n;')
				readline.parse_and_bind("tab: complete")
				readline.set_completer(comp.pathCompleter)
				if not comp:
					return -1
			return 0
		except:
			return -1

	def prompt_input(self):
		
		
			filename = str(input(" Specify File >>> "))
		

	from utils.locate_asset import locate_asset

	def initialize(self):
		if self.init_vars() != 0:
			logger.fatal("Init vars")
		if self.init_tabComplete() != 0:
			logger.fatal("Init tabcomplete")
		if self.init_classifier() != 0:
			logger.fatal("Init Classifier")
		if self.init_ocr() != 0:
			logger.fatal("Init OCR")
	

	def find_and_classify(self, filename):
		''' find the required text field from given image and read it through tesseract.
		    Results are stored in a dicionary. '''
		start = time.time()
		

		#------------------------------Classify Image----------------------------------------#

                
		logger.good("Classifying Image")
		
		coords = self.classifier.classify_image(filename)
		#lines=str(coords).split('\n')
		inf=[]
		for line in str(coords).split('\n'):
			if "sign" in line:
				continue
			if "photo" in line:
				continue
			if 'left_x' in line:
				info=line.split()
				left_x = int(info[3])
				top_y = int(info[5])
				inf.append((info[0],left_x,top_y))
		

		time1 = time.time()
		print("Classify Time: " + str(time1-start))

		# ----------------------------Crop Image-------------------------------------------#
		logger.good("Finding required text")
		cropped_images = self.locate_asset(filename, self.classifier, lines=coords)
		
		
		time2 = time.time()
		

		
		#----------------------------Perform OCR-------------------------------------------#
		
		ocr_results = None
		
		if cropped_images == []:
			logger.bad("No text found!")
			return None 	 
		else:
			logger.good("Performing OCR")
			ocr_results = self.OCR.ocr(cropped_images)
			#print(ocr_results)
			k=[]
			v=[]
			
			
			fil=filename+'-ocr'
			#with open(fil, 'w+') as f:
			for i in range(len(ocr_results)):
					
							v.append(ocr_results[i][1])
							k.append(inf[i][0][:-1])
							
			#k.insert(0,'Filename')
			#v.insert(0,filename)
			t=dict(zip(k, v))
			

		
		time3 = time.time()
		print("OCR Time: " + str(time3-time2))

		end = time.time()
		logger.good("Elapsed: " + str(end-start))
		print(t)
		return t
		
		
			
		#----------------------------------------------------------------#

	def __init__(self):
		''' Run PanOCR '''
		self.initialize()

if __name__ == "__main__":
		extracter = PanOCR()
		tim = time.time()
		
		data=[]
		for filename in os.listdir('pancards'):
			print(filename)
			filename='pancards/'+filename
			result=extracter.find_and_classify(filename)
			#print(df1)
			#df=df.append(df1)
			if result==None:
				continue
			else:
				data.append(result)
		
		df=pd.DataFrame(data)
		#print(df)
		df.to_csv (r'output/ocr_result_pan.csv', index = None, header=True,sep='\t')
		en = time.time()
		print('TOTAL TIME TAKEN',str(en-tim))
