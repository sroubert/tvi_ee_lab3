'''
*Author: Sebastian Roubert Martinez
*Last Date Modified: 12/17/2019
*The following script has two options to run: 1) python3 <name/of/this/file> new or 2) <name/of/this/file>
*running with new allows the user to take a picture, analyze, save original as 'lines.jpg', then work with GUI
*running without new allows user to work with GUI on previously taken picture
'''

import cv2
import numpy as np
import subprocess

'''
*to try with RPi 4: stream.array has much richer data native to openCV
'''


'''
takes a new picture
'''
import sys
if len(sys.argv)>2:
    print("Usage: pass either 'new' or nothing to test")
    sys.exit(1)

if (len(sys.argv) == 2):
    if (str(sys.argv[1]) == 'new'):
        cmd = "raspistill -o lines.jpg -w 400 -h 300"
        subprocess.call(cmd, shell = True)


'''
*working with GUI
'''
cv2.namedWindow('GUI', cv2.WINDOW_NORMAL)
global img
img = cv2.imread('lines.jpg')
cv2.resizeWindow('GUI',600,600)
 
v1 = 1
v2 = 1
v3 = 0
v4 = 0

def doEdgesAndLines():
    img = cv2.imread('lines.jpg')
    edges = cv2.Canny(img,v1,v2) #edge algorithm
    
    global lines
    global goodLineArray
    goodLineArray = np.empty([1,4])
    
    if ( (v1>0) & (v2>0) & (v3>0) & (v4 >0) ):
        
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,v3,v4)
        if lines is not None:
            for line in lines:
                goodLineArray = np.concatenate((goodLineArray,line),axis=0)
                for x1,y1,x2,y2 in line:
                    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.imwrite("testResults.jpg", img)
    
    
    edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    res = np.concatenate((img,edges),axis = 0)
    cv2.imshow('GUI',res)
    
    
def setVal1(val):
    global v1
    v1 = val
    doEdgesAndLines()
def setVal2(val):
    global v2
    v2 = val
    doEdgesAndLines()
def setVal3(val):
    global v3
    v3 = val
    doEdgesAndLines()
def setVal4(val):
    global v4
    v4 = val
    doEdgesAndLines()
    

cv2.createTrackbar('Edge Detection: Low Threshold','GUI',0,500,setVal1)
cv2.createTrackbar('Edge Detection: High Threshold','GUI',0,500,setVal2)
cv2.createTrackbar('Line Finding: Min Line Length','GUI',1,100,setVal3)
cv2.createTrackbar('Line Finding: Max Line Gap','GUI',1,100,setVal4)

cv2.imshow('GUI',img)
cv2.waitKey(0)
cv2.imwrite("testResults.jpg", img)


print(goodLineArray)


cv2.destroyAllWindows

#
