from mtcnn import MTCNN
import cv2 

detector = MTCNN()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    out = detector.detect_faces(frame)
    if len(out) > 0: 
        x,y, w, h = out[0]['box']

        noseX, noseY = out[0]['keypoints']['nose']
        cv2.circle(frame, center=(noseX, noseY), color=(0,255,0), thickness=1, radius = 15)

        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w, y+h), color=(200,255,122), thickness=2)
    else:
        print("No face detected")
        
    cv2.imshow('win', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()