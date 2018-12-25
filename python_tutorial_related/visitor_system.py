# File:    visitor_system.py
# Author:  JuicyITer <contactme@juicyiter.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# Copyright 2005 Duke University

# History:
## =====================
# 2018-10-27 23:08 JuicyITer <contactme@juicyiter.com> created.
## =====================


import face_recognition
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import datetime
import threading
import time
import yagmail

class Recorder:
    pass

red_dict = {}
unknownpic = []

def sendemail(title, contents, fileslist):
    yag = yagmail.SMTP("juicyiter@qq.com", 'mxb1240523210', 'smtp.qq.com', 465)
    yag.send(["contactme@juicyiter.com"], title, contents, fileslist)

def dicttostr():
    strlist = []
    listkey = list(sorted(red_dict.keys()))
    for item in listkey:
        strlist.extend([item + ',' + str(onetime) for onetime in red_dict[item].times])

    return strlist

flagover = 0

def saveRecoder(name, frame):
    global red_dict
    global flagover
    global unknownpic

    if flagover == 1:
        return

    try:
        red = red_dict[name]
        secondsDiff = (datetime.datetime.now() - red.times[-1]).total_seconds()

        if secondsDiff < 20:
            return

        red.times.append(datetime.datetime.now())
        print("Update record", red_dict, red.times)
        
    except (KeyError):
        newRed = Recorder()
        newRed.times = [datetime.datetime.now()]
        red_dict[name] = newRed
        print("Add record", red_dict, newRed.times)

    if name == 'Unknown':
        s = str(red_dict[name].times[-1])
        print("Write", s[:10] + s[-6:])
        filename = s[:10] + s[-6:] + '.jpg'

        cv2.imwrite(filename, frame)
        unknownpic.append(filename)


def loop_timer_handle():
    global timer2
    global flagover
    global red_dict
    global unknownpic

    flagover = 1
    timer2 = threading.Timer(60, loop_timer_handle)
    timer2.start()

    sendemail("Vistor records", '\n'.join(dicttostr()), unknownpic)
    print("Clear")
    red_dict.clear()
    unknownpic.clear()

    print("Restart")
    flagover = 0


timer2 = threading.Timer(2, loop_timer_handle)
timer2.start()

def load_img(sample_dir):
    for (dirpath, dirnames, filenames) in os.walk(sample_dir):
        print(dirpath, dirnames, filenames)
        facelib = []
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])

            print(filename_path)
            faceimage = face_recognition.load_image_file(filename_path)
            
            face_encoding = face_recognition.face_encodings(faceimage, known_face_locations=None, num_jitters=1)[0]
            
            facelib.append(face_encoding)
        return facelib, filenames

facelib, facename = load_img('facelib')

video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(facelib, face_encoding)
            name = 'Unknown'

            print(matches)
            if True in matches:
                first_match_index = matches.index(True)
                name = facename[first_match_index][:-4]
            face_names.append(name)
    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        #top *= 4
        #right *= 4
        #bottom *= 4
        #left *= 4
        
        cv2.rectangle = (frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        font = ImageFont.truetype('HelveticaNeue', 40)
        position = (left + 6, bottom - 6)
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, name, font = font, fill = (255, 255, 255))

        frame = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_BGR2RGB)

        saveRecoder(name, frame)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
time.sleep(2)
timer2.cancel()
