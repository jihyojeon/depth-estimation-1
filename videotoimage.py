import cv2

videopath = '/home/jihyo/Desktop/data/cam4_15fps.avi'
image_save_path = '/home/jihyo/Desktop/data/gist_people'

vidcap = cv2.VideoCapture(videopath)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(image_save_path+"/frame"+'{0:03}'.format(count)+".png", image)     # save frame as JPG file
    return hasFrames

sec = 56
end = 68
frameRate = 0.1 #//it will capture image in each frameRate second
count=1
success = getFrame(sec)

while True:
    count = count + 1
    sec = sec + frameRate
    print(sec)
    sec = round(sec, 2)
    playing = getFrame(sec)
    if sec >= end:
        break