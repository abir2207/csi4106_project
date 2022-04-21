from PIL import Image
import pytesseract
import numpy as np

filename = 'data/canada_ontario_cvo/canada_ontario_cvo_1_1.jpg' #choose an image 
img1 = np.array(Image.open(filename))
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' #Directory where Tesseract is installed
text = pytesseract.image_to_string(img1)
if not 'certifies that' in text :
    text = text.replace("Ontario","Ontario certifies that" )
    
#print(text)
hhh =text.split("that",1)[1].split("having",1)[0]
ddd = hhh.splitlines()
while '' in ddd:
    ddd.remove('')
for tx in ddd :
           
    if len(tx)<2:
        ddd.remove(tx)
print('Name: ', ddd[0])
print('Address: ', ddd[1])


