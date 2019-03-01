import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    font = ImageFont.truetype('HelveticaNeue.ttc', 40)
    draw = ImageDraw.Draw(img_PIL)

    draw.text((100, 100), "Press 'q' to exit", font = font, fill = (255, 255, 255))

    frame = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_BGR2RGB)

    cv2.imshow("capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("out.jpg", frame)
        break;

cap.release()
cv2.destroyAllWindows()
