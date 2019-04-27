#!/bin/bash

#Tested on Ubuntu 16.04.


if [ "`which sudo`" = "" ]; then
	#if we don't have sudo, grab it
	if [ "$(id -u)" != "0" ]; then
		echo "This install script needs to be run as root."
		exit -1
	fi
	echo -e "Installing Python"
	apt install -y python
	echo -e "\n\nInstalling Python Dependencies\n\n"
	apt install -y python-pip python-tk git unzip libsm6 libxext6 tesseract-ocr python-opencv libsm6 libxext6 gcc unzip wget
else
	echo -e "Installing Python"
	sudo apt install -y python
	echo -e "\n\nInstalling Python Dependencies\n\n"
	sudo apt install -y python-pip python-tk git unzip libsm6 libxext6 tesseract-ocr python-opencv libsm6 libxext6 gcc unzip
fi

pip install pillow requests opencv-python keras tensorflow matplotlib pexpect pyocr Cython fuzzywuzzy[speedup] pydocumentdb numpy



echo -e "\n\nDownloading darknet\n\n"
wget https://www.dropbox.com/s/9nxzvyyi53bi4p4/darknet?dl=0
mv darknet?dl=0 darknet
chmod 755 darknet


#needed darknet. Moved to pwd.
