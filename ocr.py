import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'#you can change path here

img = cv2.imread('ocr-a-font-sample.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))

#detecting characters


hImg,wImg,_ = img.shape
boxes =pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    #print(b)
    b=b.split(' ')
    print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,hImg-y+15),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,250),1)
cv2.imshow('Result', img)
cv2.waitKey(0)

