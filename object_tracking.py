import cv2 as cv


tracker=cv.legacy.TrackerMOSSE_create()
cap=cv.VideoCapture(0)#or the path of video


while True:
    success,img=cap.read()
    img=cv.flip(img,1)
    resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
    cv.imshow("Tracking",resize)
    if cv.waitKey(1)==113:
        break


box=cv.selectROI(resize,False)
track=tracker.init(resize,box)
cv.destroyWindow("ROI selector")

while True:

    timer = cv.getTickCount()
    track,img=cap.read()
    img=cv.flip(img,1)
    resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

    track,box=tracker.update(resize)
    if track:
        p1=(int(box[0]),int(box[1]))
        p2=(int(box[0]+box[2]),int(box[1]+box[3]))
        cv.rectangle(resize,p1,p2,(0,0,255),2,2)

    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)
    cv.putText(resize, "Fps:", (20, 40), cv.FONT_HERSHEY_PLAIN, 1.2, (255,0,255), 2)
    cv.putText(resize,str(int(fps)), (75, 40), cv.FONT_HERSHEY_PLAIN, 1.2, (0,255,0), 2)
    cv.putText(resize, "Status:", (20, 75), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 255), 2)
    cv.putText(resize, "Tracking", (100, 75), cv.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 2) 
    
        

    cv.imshow("Tracking",resize)
    if cv.waitKey(1)==113:
        break