# Video: FPS:measure of how fast the images are transitioning (40 fps: 40 images displayed in a second)

import cv2

#vid=cv2.VideoCapture(0)

vid=cv2.VideoCapture("C:/Users/akash.patwa/Downloads/smallvdo.mp4")

if(vid.isOpened()==False):
    print("unable to read the feed")

height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps= int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

#out=cv2.VideoWriter("smallvdo.mp4",cv2.VideoWriter_Fourcc(*"DIVX"),30,(width,height))
while(True):
    ret,frame=vid.read()
    cv2.imshow("video display", frame)
    #out.write(frame)
    if cv2.waitKey(20)==32:  # 32 is ASCII code of space key
     break
#vid.release()
#out.release()
cv2.destroyAllWindows()

