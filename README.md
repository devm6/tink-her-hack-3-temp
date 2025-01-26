

# [Automation using Gestures] 🎯


## Basic Details
### Team Name: Undo


### Team Members
- Member 1: Aryasree T - Gect
- Member 2: Hiba Sherin - Gect
- Member 3: Devika M B - Gect

### Hosted Project Link
[[mention your project hosted project link here]](https://drive.google.com/file/d/1rQ2NDPOpZsOwF3jnQ9V8QRg1IClvN_mM/view)

### Project Description
This project uses computer vision to interpret hand gestures from a webcam feed. It translates specific hand movements into computer actions, such as taking screenshots, simulating mouse clicks, and navigating left and right using keyboard arrows. The system is designed for hands-free control of a computer.

### The Problem statement
1. Changing Slides without using keyboard and mouse
2. Make an assistant for heavily lazy people who cant even move to press the printscreen button
   

### The Solution
Using Computer Vision

## Technical Details
### Technologies/Components Used
For Software:
- [Languages used] Python
- [Frameworks used] MediaPipe
- [Libraries used] OpenCV, PyAutoGUI,MediaPipe
- [Tools used] VSCode

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
1. High-Level Design:
The system follows a pipeline architecture. It begins by acquiring video frames from a webcam. These frames are then preprocessed (converted to RGB) and passed to the MediaPipe hand tracking model. The model outputs hand landmark data (the x, y, and z coordinates of key points on the hand). A gesture recognition module analyzes these coordinates to determine the user's gesture (e.g., distance between fingers, palm position relative to screen edges). Finally, an action execution module translates recognized gestures into actions performed by the computer through PyAutoGUI: screenshots, mouse clicks, or keyboard inputs (arrow keys in this case).
2. Detailed Implementation:
The Python code uses several libraries. Key parts of the code would be as follows:
Initialization:
Importing required libraries (cv2, mediapipe, pyautogui, numpy, time , math).
Creating a cv2.VideoCapture object to access the default webcam (index 0).
Initializing MediaPipe Hands (mp_hands.Hands).
Getting screen width/height through pyautogui.
Frame Processing Loop:
The main loop reads frames continuously from the webcam.
The frame undergoes colour conversion (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).
The frame is processed using MediaPipe to detect hand landmarks in real-time.
Landmark coordinates are extracted.
Gesture Recognition Logic:
For this particular example, this entails calculating the distance between the index fingertip and the middle fingertip and applying threshold conditions to trigger click and screenshot functionality
Another calculation, which is the relative screen centre position, from the x-axis of palm-centre, triggers left/right arrow key presses. Moving averages or Kalman filtering can be applied to deal with jerky hand motions.
Action Execution:
PyAutoGUI is used to simulate actions like pyautogui.click(), pyautogui.hotkey("win", "prtsc"), and pyautogui.press('left'/'right') based on identified gestures. A small time delay might be helpful to avoid repetitive actions.
Visualization:
cv2.imshow() function to display the captured and processed frames (typically highlighting the landmarks detected on the hand). Text might overlay information (e.g., distances).


# Installation
[commands] pip install opencv-python mediapipe pyautogui numpy


# Run
[commands] python printsc.py
           python changeppt.py

### Project Documentation
For Software:
1. Core Functionality:
Screenshot Capture: A specific gesture (typically a widening distance between index and middle finger) triggers a screenshot.
Mouse Click Simulation: A different gesture (typically a narrowing distance between index and middle finger) simulates a mouse click.
Left/Right Arrow Navigation: The horizontal position of the palm relative to the center of the screen controls left and right arrow key presses, allowing for basic screen navigation.

2.Algorithm
Capture a frame from the webcam.
Process the frame using MediaPipe's hand detection model.
Extract relevant landmark coordinates.
Apply algorithms (distance calculations, screen-relative position analysis) to determine gestures.
Based on the determined gesture, execute corresponding actions using PyAutoGUI.
Display the processed video feed with visual feedback (landmarks drawn, distance shown).



# Screenshots (Add at least 3)
![Screenshot1]![learning](https://github.com/user-attachments/assets/ca98492e-a0ab-4f59-8b2c-07fcb5178e55)

*learning the basics-videocapture using OpenCV*

![Screenshot2]![hkcoordi](https://github.com/user-attachments/assets/04a20777-d661-487a-a0de-afece2afe26d)

*Recognition of 21 hand-knuckle coordinates*

![Screenshot3]![changing ppt](https://github.com/user-attachments/assets/f8be00e9-a9c4-43d8-9d3f-b981c5b60b8d)

*Changing ppt slides without using keyboard or mouse*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Team](Add photo of your team here)


![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[[Add your demo video link here]](https://drive.google.com/file/d/1rQ2NDPOpZsOwF3jnQ9V8QRg1IClvN_mM/view?usp=sharing)
*Demo of changing fast-forwarding/backwarding (5 sec) YouTube video, changing slides a pdf/ppt by showing palm centre on right side or left side*

# Additional Demos
[[Add any extra demo materials/links]](https://drive.google.com/file/d/14tO4MJhocffxQpLa0u1qwuOO7FAEmhkG/view?usp=sharing)
*Demo of taking screenshot using 'cut' [victory with movement] gesture


## Team Contributions
- Devika M B:  Done relevant research and studies related to Open CV and implemented it in programs. Implemented print-screen using Open CV.
- Aryasree T: Implemented the program for using right arrow key and left arrow key with Open C V.
- Hiba sherin: Implented the program for using right arrow key and left arrow key with Open C V.Done the research for this program.

---
Made with ❤️ at TinkerHub




