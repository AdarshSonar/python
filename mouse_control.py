import cv2               # opencv-contrib-python
import face_recognition as mp
# import mediapipe as mp    # mediapipe
import pyautogui          # PyAutoGUI
                
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size() # adjusting screen dimensions

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converting color to RGB
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    #print(landmark_points)
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]): #enumerate - 1.Id or index  
            x = int(landmark.x * frame_w)                         # 2. element or landmark
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3 , (0,255,0)) # green circle
            # print(x,y)
            if id ==1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h/ frame_h * y
                pyautogui.moveTo(screen_x,screen_y)
                
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)                         # 2. element or landmark
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3 , (0,255,255)) # yellow circle
        # print(left[0].y - left[1].y)
        if (left[0].y - left[1].y) < 0.004:
            # print('click')
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)  # imshow - image show
    cv2.waitKey(1)