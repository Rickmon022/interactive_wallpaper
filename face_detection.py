from mtcnn import MTCNN
import cv2 
import subprocess
import os

detector = MTCNN()
cap = cv2.VideoCapture(0)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

wallpapers = {
    "left4": "assets/left4.png",
    "left3": "assets/left3.png",
    "left2": "assets/left2.png",
    "left1": "assets/left1.png",
    "center": "assets/center.png",
    "right1": "assets/right1.png",
    "right2": "assets/right2.png",
    "right3": "assets/right3.png",
    "right4": "assets/right4.png"
}

def set_wallpaper(direction):
    image_path = os.path.join(BASE_DIR, wallpapers[direction])

    result = subprocess.run(
        ["caelestia", "wallpaper", "-f", image_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Wallpaper error:", result.stderr)
        return False

    return True

curr_dir = "center"
set_wallpaper("center")

while True:
    ret, frame = cap.read()
    out = detector.detect_faces(frame)
    if len(out) > 0:
        # my webcam resolution = (640,480)
        cx, cy = (320, 240)

        # face coordinates 
        x,y, w, h = out[0]['box']

        # using nose as the centre point of face
        noseX, noseY = out[0]['keypoints']['nose']

        dx, dy = (noseX-cx, noseY-cy)
        # print(x, y)
        # print(dx, dy)

        if dx < -175:
            dir = "right1"
        elif dx < -150:
            dir = "right2"
        elif dx < -100:
            dir = "right3"
        elif dx < -50:
            dir = "right4"
        elif dx < 50:
            dir = "center"
        elif dx < 100:
            dir = "left1"
        elif dx < 150:
            dir = "left2"
        elif dx < 200:
            dir = "left3"
        else:
            dir = "left4"

        if dir != curr_dir:
            set_wallpaper(dir)
            curr_dir = dir

        cv2.circle(frame, center=(noseX, noseY), color=(0,255,0), thickness=1, radius = 15)
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,0), thickness=2)
        
    cv2.imshow('win', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()