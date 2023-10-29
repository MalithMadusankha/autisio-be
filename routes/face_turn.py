from fastapi import APIRouter, UploadFile, HTTPException
import os
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

face = APIRouter()

@face.post('/father/facce-turn')
async def upload_file(file: UploadFile):
    print("<=============== Face Turn ==================>")
    result = 0
    if file:
        # Using relative path
        directory_path = 'face_video'

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_path_webm = os.path.join(directory_path, 'faceturn.webm')
        with open(file_path_webm, "wb") as f:
            f.write(file.file.read())

        # Check if file exists
        if not os.path.exists(file_path_webm):
            print("Error: File not saved!")
            raise HTTPException(status_code=500, detail="File saving error")

        # Convert WebM to MP4 using OpenCV
        file_path_mp4 = os.path.join(directory_path, 'faceturn.mp4')

        try:
            cap = cv2.VideoCapture(file_path_webm)
            mp_face_mesh = mp.solutions.face_mesh
            index = 0

            with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5,
            ) as face_mesh:

                while cap.isOpened():
                    success, imgf = cap.read()
                    if not success:
                        break

                    img = cv2.flip(imgf, 1)
                    results = face_mesh.process(img)

                    if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
                        for face_landmarks in results.multi_face_landmarks:
                            if index == 0:
                                prevX = int(face_landmarks.landmark[0].x * img.shape[1])
                            index = index + 1
                            x = int(face_landmarks.landmark[0].x * img.shape[1])

                            sum = prevX - x
                            if sum > -20 and sum < 20:
                                # center
                                result += 0
                            elif sum < -20:
                                # right
                                result -= 1
                            elif sum > 20:
                                # left
                                result += 1

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("Error in video conversion (OpenCV):", str(e))
            raise HTTPException(status_code=500, detail="Conversion error (OpenCV)")

        print(" Done ", result)
        return {"msg": result}
    else:
        raise HTTPException(status_code=400, detail="No file uploaded")

@face.post('/mother/facce-turn')
async def upload_file(file: UploadFile):
    print("<=============== Face Turn ==================>")
    result = 0
    if file:
        # Using relative path
        directory_path = 'face_video'

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_path_webm = os.path.join(directory_path, 'faceturn.webm')
        with open(file_path_webm, "wb") as f:
            f.write(file.file.read())

        # Check if file exists
        if not os.path.exists(file_path_webm):
            print("Error: File not saved!")
            raise HTTPException(status_code=500, detail="File saving error")

        # Convert WebM to MP4 using OpenCV
        file_path_mp4 = os.path.join(directory_path, 'faceturn.mp4')

        try:
            cap = cv2.VideoCapture(file_path_webm)
            mp_face_mesh = mp.solutions.face_mesh
            index = 0

            with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5,
            ) as face_mesh:

                while cap.isOpened():
                    success, imgf = cap.read()
                    if not success:
                        break

                    img = cv2.flip(imgf, 1)
                    results = face_mesh.process(img)

                    if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
                        for face_landmarks in results.multi_face_landmarks:
                            if index == 0:
                                prevX = int(face_landmarks.landmark[0].x * img.shape[1])
                            index = index + 1
                            x = int(face_landmarks.landmark[0].x * img.shape[1])

                            sum = prevX - x
                            if sum > -20 and sum < 20:
                                # center
                                result += 0
                            elif sum < -20:
                                # right
                                result -= 1
                            elif sum > 20:
                                # left
                                result += 1

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("Error in video conversion (OpenCV):", str(e))
            raise HTTPException(status_code=500, detail="Conversion error (OpenCV)")

        print(" Done ", result)
        return {"msg": result}
    else:
        raise HTTPException(status_code=400, detail="No file uploaded")
