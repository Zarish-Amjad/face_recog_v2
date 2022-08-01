import pickle
import sys
import os

registered_path = '/var/www/html/api_orio/Face_recog_v2/Registered/'
encodings_file_path = '/var/www/html/api_orio/Face_recog_v2/encodings.dat'
ar_args = sys.argv
key = int(ar_args[1])

all_face_encodings = {}
try:
    with open(encodings_file_path, 'rb') as f:
        all_face_encodings = pickle.load(f)
except:
    pass

try:
    all_face_encodings.pop(key)
    with open(encodings_file_path, 'wb') as f:
        pickle.dump(all_face_encodings, f)
    os.remove(registered_path + str(key) + ".jpg")
except:
    print("Something went wrong")
    quit()

print(list(all_face_encodings.keys()))
