import cv2
import numpy as np

pallete = [[0,0,0],[0,0,255],[0,255,0],[255,0,0],[0,255,255],
           [255,0,255],[255,255,0],[255,255,255]]
color = [255,255,255]
sel = 0
dot = 4

img = np.zeros((512,512,3), np.uint8)

def draw_circle(event,x,y,flags,param):
    global color, sel, dot
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if x > 120 + dot:
            if sel == 0:
                cv2.rectangle(img, (x-dot,y-dot),(x+dot,y+dot), color, -1)
            else:
                cv2.circle(img, (x,y), dot+1, color, -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        if x > 0 and x < 120 + dot:
            if y > 0 and y < 240:
                inx = int(x / 60)
                iny = int(y / 60)

                color = pallete[inx*4 + iny]
                cv2.rectangle(img, (10, 310), (50, 350), color, -1)
                cv2.circle(img, (90, 330), 20, color, -1)
            elif y > 300 and y < 360:
                inx = int(x / 60)
                if inx == 0:
                    cv2.rectangle(img, (10-3, 310-3), (50+3, 350+3), [255,255,255], 2)
                    cv2.circle(img, (90, 330), 20+3, [0,0,0], 2)
                    sel = 0
                else:
                    cv2.rectangle(img, (10-3, 310-3), (50+3, 350+3), [0,0,0], 2)
                    cv2.circle(img, (90, 330), 20+3, [255,255,255], 2)
                    sel = 1
        else:
            if sel == 0:
                cv2.rectangle(img, (x-dot,y-dot),(x+dot,y+dot), color, -1)
            else:
                cv2.circle(img, (x,y), dot+1, color, -1)

                
for x in range(0,2):
    for y in range(0, 4):
        img = cv2.rectangle(img, (x*60, y*60), (x * 60 + 60, y * 60 + 60),
                            pallete[x*4 + y], -1)

cv2.rectangle(img, (0, 300), (60, 360), (255,255,255), 2)
cv2.rectangle(img, (10, 310), (50, 350), color, -1)
cv2.rectangle(img, (60, 300), (120, 360), (255,255,255), 2)
cv2.circle(img, (90, 330), 20, color, -1)
cv2.rectangle(img, (10-3, 310-3), (50+3, 350+3), [255,255,255], 2)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
