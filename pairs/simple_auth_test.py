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

start = time.process_time()
userID_image = face_recognition.load_image_file(id1+".jpg")
print(time.process_time() - start)

start = time.process_time()
current_image = face_recognition.load_image_file(path2+".jpg")
print(time.process_time() - start)

start = time.process_time()
userID_image_encoding = face_recognition.face_encodings(userID_image)[0]
print(time.process_time() - start)
start = time.process_time()
current_image_encoding = face_recognition.face_encodings(current_image)[0]
print(time.process_time() - start)

start = time.process_time()
results = face_recognition.compare_faces([userID_image_encoding], current_image_encoding,  tolerance=0.40)
print(time.process_time() - start)
print(results[0])
print(face_recognition.face_distance([userID_image_encoding], current_image_encoding))
