from imutils.perspective import four_point_transform
import pytesseract
import argparse
import imutils
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input receipt image")
ap.add_argument("-d", "--debug", type=int, default=-1,
                help="whether or not we are visualizing each step of the pipeline")
args = vars(ap.parse_args())

# load the input image from disk, resize it, and compute the ratio
# of the *new* width to the *old* width
orig = cv2.imread(args["image"])
image = orig.copy()
image = imutils.resize(image, width=1500)
ratio = orig.shape[1] / float(image.shape[1])

# convert the image to grayscale, blur it slightly, and then apply
# edge detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 300)
# check to see if we should show the output of our edge detection
# procedure
if args["debug"] > 0:
    cv2.imshow("Input", image)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)

ret, thresh1 = cv2.threshold(gray, 0 , 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
file = open("recognized.txt", "w+")
file.write("")
file.close()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(image, (x,y), (x + w, y + h), (0, 255, 0), 2)
    cropped = image[y:y + h, x:x + w]
    file = open("recognized.txt", "a")
    text = pytesseract.image_to_string(cropped)
    file.write(text)
    file.write("\n")
    file.close()
