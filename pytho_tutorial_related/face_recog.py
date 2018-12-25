from PIL import Image, ImageDraw

import face_recognition

image = face_recognition.load_image_file("2.jpg")

face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image)
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width = 5)
pil_image.show()
