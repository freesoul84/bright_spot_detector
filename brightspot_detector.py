#importing all libraries
import cv2
#webcam captrure
cam = cv2.VideoCapture(0)
#counter
count = 0
#directions
print("INSTRUCTIONS :")
print("1.press s for saving window")
print("2.press q for closing window")

#frame captures
while True:
    r, frame = cam.read()
    #frame showing
    cv2.imshow("image", frame)
    k = cv2.waitKey(1)
    #quit "q"
    if k==ord("q"):
        print("Closed...")
        break
    #save "s"
    elif k==ord("s"):
        #image name"
        image_name = "bright_spot_{}.png".format(count)
        #converting image into grey scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # largest intensity value area (approx)
        (minv, maxv, minl, maxl) = cv2.minMaxLoc(gray)
  
        cv2.circle(frame, maxl, 10, (0,255, 0), 2)
        #image saving
        cv2.imwrite(image_name,frame)
        print("{} is saved".format(image_name))
        #result
        cv2.imshow("image_spot",frame)
        count+= 1
    if not r:
        break

cam.release()
cv2.destroyAllWindows()
