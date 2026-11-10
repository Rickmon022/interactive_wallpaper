# Interactive Wallpaper

A desktop wallpaper that reacts to where you are. Move your head left or right in front of the webcam and the wallpaper shifts perspective in real time, creating a 3D parallax effect.

![Preview](assets/preview.gif)

## How It Works

1. The webcam feed is read frame by frame with **OpenCV**.
2. **MTCNN** detects the face and its facial keypoints.
3. The nose position is compared with the frame centre to get a horizontal offset.
4. The offset is mapped to one of **9 pre-rendered wallpaper angles** (`left1-4`, `center`, `right1-4`).
5. The wallpaper only changes when the angle bucket changes, which avoids redundant updates.

```
Webcam -> MTCNN face + nose -> offset from centre -> angle bucket -> set wallpaper
```

## Tech Stack

- **Language:** Python
- **Computer vision:** OpenCV, MTCNN (TensorFlow/Keras)
- **System integration:** [Caelestia](https://github.com/caelestia-dots) CLI for setting the wallpaper on Linux

## Getting Started

### Prerequisites

- Linux with the `caelestia` CLI installed and available on your `PATH`
- A webcam (tuned for 640x480)
- Python 3.10+

### Installation

```bash
git clone https://github.com/Rickmon022/interactive_wallpaper.git
cd interactive_wallpaper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python face_detection.py
```

A preview window shows the detected face and nose point. Press **x** to quit.

## Project Structure

```
interactive_wallpaper/
├── face_detection.py   # Face tracking and wallpaper switching
├── assets/             # 9 wallpaper frames (left1-4, center, right1-4)
└── requirements.txt
```

## Configuration

Thresholds live in `face_detection.py`. The nose offset `dx` (in pixels) is mapped like this:

| Offset (dx) | Wallpaper |
|---|---|
| -50 to 50 | `center` |
| below -50 | `right4` to `right1` (steps at -50, -100, -150, -175) |
| above 50 | `left1` to `left4` (steps at 50, 100, 150, 200) |

Adjust the thresholds or swap the images in `assets/` to change sensitivity or style.

## Limitations and Future Work

- Assumes a 640x480 webcam; the frame centre is hardcoded
- Wallpaper changes in discrete steps rather than smoothly
- Currently depends on the Caelestia CLI; support for other desktop environments is planned
- Ideas: vertical tracking, smoothing between frames, a lighter face detector for lower CPU usage

## What I Learned

- Real-time face detection and keypoint tracking with OpenCV and MTCNN
- Mapping continuous input to discrete states with threshold logic
- Integrating a Python script with a system CLI via `subprocess`

## Author

**Rickmon** - B.Tech CSE, IIIT Una
[GitHub](https://github.com/Rickmon022)
