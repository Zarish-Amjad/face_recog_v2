import pickle

encodings_file_path = '/var/www/html/api_orio/Face_recog_v2/encodings.dat'

all_face_encodings = {}
try:
    with open(encodings_file_path, 'rb') as f:
        all_face_encodings = pickle.load(f)
except:
    pass

print(list(all_face_encodings.keys()))