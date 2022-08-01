import face_recognition
import sys

ar_args = sys.argv
id1 = str(ar_args[1])
path2 = str(ar_args[2])
registered_path = "/var/www/html/api_orio/Face_recog_v2/Registered/"

userID_image = face_recognition.load_image_file(registered_path + id1 + ".jpg")
current_image = face_recognition.load_image_file(path2)

userID_image_encoding = face_recognition.face_encodings(userID_image)[0]
current_image_encoding = face_recognition.face_encodings(current_image)

if len(current_image_encoding) >= 1:
    current = current_image_encoding[0]
    results = face_recognition.compare_faces(
        [userID_image_encoding], current,  tolerance=0.40)
    print(results[0])
else:
    print("No Face Found")
