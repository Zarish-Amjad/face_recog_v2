import face_recognition
# import cv2
import numpy as np
import time
import os
import sys
# from skimage.io import imread_collection
import numpy as np
# import pandas as pd
import statistics
import time

ar_args = sys.argv
id1 = str(ar_args[1])
#id2 = str(ar_args[1])
path2= str(ar_args[2])

userID_image = face_recognition.load_image_file("//var//www//html//api_orio//Face_recog_v2//"+id1+".jpg")

current_image = face_recognition.load_image_file("//var//www//html//api_orio//Face_recog_v2//"+path2+".jpg")

userID_image_encoding = face_recognition.face_encodings(userID_image)[0]
start = time.process_time()
current_image_encoding = face_recognition.face_encodings(current_image, num_jitters=2)
if(len(current_image_encoding)>=1):
    current=current_image_encoding[0]
    results = face_recognition.compare_faces([userID_image_encoding], current,  tolerance=0.40)
    print(results[0])
    print(face_recognition.face_distance([userID_image_encoding], current))
else:
    print("No Face Found")

