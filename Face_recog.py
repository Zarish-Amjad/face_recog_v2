import face_recognition
import cv2
import numpy as np
import time
import os
from skimage.io import imread_collection
import numpy as np
import sys
#from byt_arr import bytetoimage

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

images = '/var/www/html/api_orio/Face_recog_v2/Registered/'
old_dir = '/var/www/html/api_orio/Face_recog_v2'
db = os.chdir(images)
images = os.listdir(db)
#os.chdir(old_dir)


known_face_encodings = []
known_face_names = []
for image in images:
    img = face_recognition.load_image_file('/var/www/html/api_orio/Face_recog_v2/Registered/'+str(image))
    img_encoding = face_recognition.face_encodings(img)[0]
    known_face_encodings.append(img_encoding)
for image in images:
    name = image.split('.jpg')
    known_face_names.append(name)

#Remove empty string form the names list
known_face_names = np.concatenate(known_face_names, axis=0)
known_face_names = [i for i in known_face_names if i]

def camera_init():
    video_capture = cv2.VideoCapture(0)


# Get a reference to webcam #0 (the default one)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
preview = 0
def face_recog(byte_array, width, height):
    while True:
        # Grab a single frame of video
        img=cv2.imread(byte_array, 0)
        #ret, frame = bytetoimage(img, width, height, channels = 3)
        #if ret == False:
        #    continue

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                print(name)

def Register_face(person_name):
    global process_this_frame
    global preview
    while True:
        preview +=1
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        cv2.imshow('Frame',frame)
        cv2.waitKey(1)
        #time.sleep(5)
        #print(len(face_locations))
        #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #rgb_small_frame = small_frame[:, :, ::-1]
        if preview == 100:
            if face_locations:
                cv2.imwrite('/var/www/html/api_orio/Face_recog_v2/Registered/'+str(person_name)+'.jpg', frame)
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



def Run_pro():
    value = int(input("Press {} for Face recognition model\nPress {} to register new face\n".format(1, 2)))
    if value == 1:
        face_recog(byte_array, width, height)
    if value == 2:
        name = input("Write name of the person without space\n")
        Register_face(name)
    else:
        print('You pressed wrong value, Try again')
        Run_pro()

def bytetoimage(array_image, width, height, channels = 3):
    flat_image = np.array(array_image)
    image = flat_image.reshape(width, height, channels)
    return True, image

def string_to_bytearray(string):
    b_array = bytearray(string.encode())
    ar= list()
    for elem in b_array:
        ar.append(elem)
    return ar
def byteArray_from_path(path):
    img = cv2.imread(path, 0) 


ar_args= sys.argv
width= sys.argv[3]
height= sys.argv[2]
str_bytes= sys.argv[1]
print(ar_args)

face_recog(str_bytes, int(width), int(height))