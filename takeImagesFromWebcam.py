import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

path_to_save = #FILL HERE

i = 0
while True:
    suc, img = cap.read()
    if not(suc):
        break

    nameImg = "A" + str(i) + ".png"

    #Save image when "q" is pressed
    if cv.waitKey(30) & 0xFF == ord('q'):
        cv.imwrite(path_to_save + nameImg,img)
    
    #Show webcam
    cv.imshow("img",img)

    #Increment i for name of image to be saved
    i = i + 1

    #break on ESC
    if cv.waitKey(30) & 0xFF == 27:
        break
