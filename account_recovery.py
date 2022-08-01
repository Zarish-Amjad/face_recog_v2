import face_recognition
import pickle
import numpy as np
import sys

encodings_file_path = '/var/www/html/api_orio/Face_recog_v2/encodings.dat'

ar_args = sys.argv
path = str(ar_args[1])

all_face_encodings = {}
try:
    with open(encodings_file_path, 'rb') as f:
        all_face_encodings = pickle.load(f)
except:
    pass

current_image = face_recognition.load_image_file(path)
current_image_encoding = face_recognition.face_encodings(current_image)

if len(current_image_encoding) >= 1:
    if len(all_face_encodings) > 0:
        saved_image_encodings = np.array(list(all_face_encodings.values()))
        results = face_recognition.compare_faces(
            saved_image_encodings, current_image_encoding[0],  tolerance=0.40)
        index = (np.where(results)[0])[0]
        val = list(all_face_encodings.keys())[index]
        # print(results)
        # print(index)
        print(val)
    else:
        print("No User Found")
else:
    print("No Face Found")
