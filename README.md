![OCR](OCR.png?raw=true "Title")

# PAN_OCR
To understand the building process please go through my blog [here.](https://medium.com/saarthi-ai/how-to-build-your-own-ocr-a5bb91b622ba)
Run below command to install darknet.

```bash ./darknet.sh```

You need to have tesseract installed to run this OCR.
Now move your data folder and weight file in this repository. 
To run the OCR follow this command.

``` pan.py -d -t ```

You can see the results in output folder in form of a csv file.

You can find pretrained model [here](https://drive.google.com/file/d/11amAIKcERA4odgIflVAw7inKPFR0ylRL/view?usp=sharing)
