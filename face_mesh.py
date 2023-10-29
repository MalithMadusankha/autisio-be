import cv2
import mediapipe as mp

print(mp.__version__)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

text = "Center"
position = (50, 50)  # (x, y) coordinates of the top-left corner of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # BGR color (red in this example)
line_type = 2  # Line thickness

index = 0
prevX = 0

# custome style
my_drawing_spec = mp_drawing_style.DrawingSpec(color = (0,255,0), thickness = 1)

cap = cv2.VideoCapture(0)

mp_face_mesh = mp.solutions.face_mesh
 
with mp_face_mesh.FaceMesh(
    max_num_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5,
    ) as face_mesh:
 
    while cap.isOpened():
        success_, imgf = cap.read()
        img = cv2.flip(imgf,1)
        results = face_mesh.process(img)
        
        if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:

            for face_landmarks in results.multi_face_landmarks:
                # mp_drawing.draw_landmarks(
                #     image = img,
                #     landmark_list = face_landmarks,
                #     connections = mp_face_mesh.FACEMESH_TESSELATION,
                #     landmark_drawing_spec = None,
                #     connection_drawing_spec = mp_drawing_style.get_default_face_mesh_tesselation_style()
                # )
                
                if index == 0:
                    prevX = int(face_landmarks.landmark[0].x * img.shape[1])
                index = index + 1
                x = int(face_landmarks.landmark[0].x * img.shape[1])
                y = int(face_landmarks.landmark[0].y * img.shape[0])
                
                sum =  prevX - x               
                if sum > -20 and sum < 20:
                    text = "Center"
                elif sum < -20:
                    text = "Right"
                elif sum > 20:
                    text = "Left"
                
                cv2.putText(img, text, position, font, font_scale, font_color, line_type)

                cv2.circle(img, (x, y), 7, (255, 255, 0), -1)
                mp_drawing.draw_landmarks(
                    image = img,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_style.get_default_face_mesh_contours_style()
                )
        
        if not success_:
            break
        
        cv2.imshow("face detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()