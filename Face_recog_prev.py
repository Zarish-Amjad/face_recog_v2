#!/usr/bin/python
# -*- coding: utf-8 -*-
# !pip install face_recognition

import face_recognition
import cv2
import numpy as np
import time
import os
import sys
from skimage.io import imread_collection
import numpy as np
import pandas as pd
import statistics

images = '/var/www/html/api_orio/Face_recog_v2/Registered'

# old_dir = '/var/www/api_orio/Face_recog_v2'

db = os.chdir(images)
images = os.listdir(db)

# os.chdir(old_dir)

known_face_encodings = []
known_face_names = []
for image in images:
    img = \
        face_recognition.load_image_file('/var/www/html/api_orio/Face_recog_v2/Registered/'
             + str(image))
    encod_array = face_recognition.face_encodings(img)
    if len(encod_array) > 0:
        img_encoding = encod_array[0]
        name = image.split('.jpg')
        known_face_names.append(name)
        known_face_encodings.append(img_encoding)

# Remove empty string form the names list

known_face_names = np.concatenate(known_face_names, axis=0)
known_face_names = [i for i in known_face_names if i]

# Initialize some variables

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
preview = 0


def face_recog(byte_array, width, height):

    # print("####iter")
    # Grab a single frame of video

    (ret, frame) = bytetoimage(byte_array, width, height, channels=3)
    rgb_small_frame = frame[:, :, ::-1]

    # Only process every other frame of video to save time
    # Find all the faces and face encodings in the current frame of video

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,
            face_locations)
    face_names = []
    for face_encoding in face_encodings:

        # See if the face is a match for the known face(s)

        matches = face_recognition.compare_faces(known_face_encodings,
                face_encoding)
        name = 'Unknown'
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

        # determine the recognized face with the largest number
        # of votes (note: in the event of an unlikely tie Python
        # will select first entry in the dictionary)

            #name = max(counts, key=counts.get)
        face_names.append(name)
    print(face_names)


        #
        # Or instead, use the known face with the smallest distance to the new face
##        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
##        best_match_index = np.argmin(face_distances)
##        if matches[best_match_index]:
##            name = known_face_names[best_match_index]
##
##        face_names.append(name)

def Register_face(person_name):
    global process_this_frame
    global preview
    while True:
        preview += 1
        (ret, frame) = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        cv2.imshow('Frame', frame)
        cv2.waitKey(1)

        # time.sleep(5)
        # print(len(face_locations))
        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame = small_frame[:, :, ::-1]

        if preview == 100:
            if face_locations:
                cv2.imwrite('/var/www/api_orio/public_html/public/images/'
                             + str(person_name) + '.jpg', frame)
                print('Face Image written successfully\nChanges will take effect in 10 seconds')
                cv2.destroyAllWindows()
                time.sleep(10)
                break
            else:
                preview = 0
                Run_pro()
                print('No face detected')
        else:

            continue

        # Release handle to the webcam

    video_capture.release()
    cv2.destroyAllWindows()


def string_to_bytearray(string):
    b_array = bytearray(string.encode())
    ar = list()
    for elem in b_array:
        ar.append(elem)
    return ar


def bytetoimage(
    array_image,
    width,
    height,
    channels=3,
    ):
    flat_image = np.array(array_image)
    image = flat_image.reshape(width, height, channels)
    return (True, image)


def Run_pro():
    f = open(str(sys.argv[0]), 'rb')
    width = sys.argv[0]
    height = sys.argv[0]
    image_bytes = f.read()
    decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    byte_array = decoded

    value = 1
    if value == 1:
        face_recog(byte_array, width, height)
    else:

    # if value == 2:
    #     name = input("Write name of the person without space\n")
    #     Register_face(name)

        print('You pressed wrong value, Try again')
        Run_pro()


ar_args = sys.argv
width = sys.argv[3]
height = sys.argv[2]
f = open(str(sys.argv[1]), 'rb')
image_bytes = f.read()
decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

face_recog(decoded, int(width), int(height))
