import cv2 as cv

path_to_video = #FILL HERE
path_to_save = #FILL HERE
cap = cv.VideoCapture(path_to_video)

i = 100
while True:
    sucess, img = cap.read()
    if not(sucess):
        break
        
    #Name of image to be saved
    nameImg = "A" + str(i) + ".jpg"

    #Save an image every 5 frames
    if i%5 == 0:
        cv.imwrite(path_to_save + nameImg,img)

    #Increment i for name of image to be saved
    i = i +1






