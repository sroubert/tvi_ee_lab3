import time
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(10)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # At this point the image is available as stream.array
        image = stream.array




cv2.namedWindow('GUI', cv2.WINDOW_NORMAL)
cv2.resizeWindow('GUI',600,600)
 


#img = cv2.imread(image)
cv2.imshow('GUI',image)

cv2.waitKey(0)
cv2.destroyAllWindows
