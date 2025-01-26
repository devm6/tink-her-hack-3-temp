

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




