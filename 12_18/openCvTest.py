# # Testing threshold for line detection
import cv2
import numpy as np

cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Result',600,600)



img = cv2.imread('lines.jpg')

#STUDENT EDIT BASED ON GUI RESULTS
edges = cv2.Canny(img,11,33)


# In[11]:


minLineLength = 3 #Minimum length of line. Line segments shorter than this are rejected.
maxLineGap = 30 #Maximum allowed gap between line segments to treat them as single line.
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)


# In[12]:


for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
#        cv2.waitKey(0)
        cv2.imshow('Result',img)
        cv2.waitKey(0)
        #input('num')

#print(lines)

# In[13]:


#cv2.imshow('Result',img)
# cv2.waitKey(0)

print(lines)

cv2.imwrite("testResults.jpg", img)
cv2.destroyAllWindows


# In[14]:



# In[ ]:




