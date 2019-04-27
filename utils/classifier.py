from abc import ABC, abstractmethod
from typing import Tuple

class Classifier(ABC):
	@abstractmethod
	def initialize(self):
		''' Initialize the classifier '''
		pass

	@abstractmethod
	def classify_image(self, image):
		''' Classify an image.
		Input: An image, opened by PIL'''
		pass

	@abstractmethod
	def extract_info(self, line:str) -> Tuple:
		''' Extract the information from a line returned by the classifier. 
		Ex: Many programs do not return in an easily readable format, and need to be parsed.
		For example, a line could be: "label (90%) x:1300 y:3400 height:300 width:900". This
		should return the area of the bounding box. '''
		pass

	def __init__(self):
		self.initialize()
