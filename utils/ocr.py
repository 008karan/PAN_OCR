from abc import ABC, abstractmethod
from typing import List
import threading

class OCR(ABC):
	@abstractmethod
	def initialize(self):
		''' Initialize the OCR '''
		pass

	@abstractmethod
	def ocr_one_image(self, images:List) -> List:
		''' OCR an image.
		Input: An array of (area, image)s, opened by PIL and pre-processed
		Return: An array of (area, message), where the message is from OCR'''
		pass

	def ocr(self, images:List) -> List:
		'''Sends an opened image to Azure's cognitive services.
		Input: images (tuple(area, image))
		Returns the results from Tesseract.'''
		threads = []
		threadResults = ["" for i in range(len(images))]
		threadNum = 0
		results = []
		for image in images:
			t = threading.Thread(target=self.ocr_one_image, args=(image[0], image[1]), kwargs={'threadList':threadResults, 'threadNum':threadNum})

			t.start()
			threads.append(t)
			threadNum += 1

		for t in threads:
			t.join()
		i = 0
		for result in threadResults:
			results.append((images[i][0], result))
			i += 1
		return results

	def __init__(self):
		self.initialize()
