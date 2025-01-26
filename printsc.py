import cv2 as cv
import mediapipe as mp
import pyautogui
from math import hypot

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture video from the webcam
cap = cv.VideoCapture(0)

# Previous distance to determine gesture action
previous_distance = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for a mirror effect
    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            h, w, _ = frame.shape  # Get frame dimensions
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            
            cv.circle(frame, (middle_x, middle_y), 10, (255, 0, 0), cv.FILLED)
            cv.circle(frame, (index_x, index_y), 10, (255, 0, 0), cv.FILLED)

            
            cv.line(frame, (middle_x, middle_y), (index_x, index_y), (0, 255, 0), 3)

           
            distance = hypot(index_x - middle_x, index_y - middle_y)

           
            if previous_distance == 0:
                previous_distance = distance

            if abs(distance - previous_distance) > 20:  # Threshold to avoid small fluctuations
                if distance > previous_distance:
                    pyautogui.hotkey("win","prtsc")
                else:
                    pyautogui.press("click")
                previous_distance = distance

            # Display the distance value on the frame
            cv.putText(frame, f"Distance: {int(distance)}", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow("Gesture Screenshot Control", frame)
    if cv.waitKey(1) & 0xFF == ord('k'):
        break

cap.release()
cv.destroyAllWindows()
hands.close()