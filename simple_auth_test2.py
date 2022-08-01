# python3 simple_auth_test2.py /var/www/html/api_orio/Face_recog_v2/610.jpg
import face_recognition
import pickle
import numpy as np
import sys

encodings_file_path = '/var/www/html/api_orio/Face_recog_v2/encodings.dat'

ar_args = sys.argv
path = str(ar_args[1])
key = int(ar_args[2])

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
        if(any(results)):
            print("Face already registered")
        else:
            # id = len(all_face_encodings)
            all_face_encodings[key] = current_image_encoding[0]
            try:
                with open(encodings_file_path, 'wb') as f:
                    pickle.dump(all_face_encodings, f)
                # print(str(id) + ",Face Not Registered")
                print("Face Not Registered")
            except:
                print("Something went wrong")
    else:
        # id = len(all_face_encodings)
        all_face_encodings[key] = current_image_encoding[0]
        try:
            with open(encodings_file_path, 'wb') as f:
                pickle.dump(all_face_encodings, f)
            # print(str(id) + ",No User Found")
            print("No User Found")
        except:
            print("Something went wrong")
else:
    print("No Face Found")


# basepath = "/var/www/html/api_orio/Face_recog_v2/Registered"
# print(all_face_encodings)

# print(len(all_face_encodings))

# all_face_encodings[len(all_face_encodings)] = current_image_encoding[0]
# with open(encodings_file_path, 'wb') as f:
#     pickle.dump(all_face_encodings, f)

# encodings_read_file = open(encodings_file_path, 'r')
# lines = encodings_read_file.readlines()
# for line in encodings_read_file:
#     print(line.strip())
# encodings_read_file.close()

# encodings_write_file = open(encodings_file_path, 'w')
# new_picks = current_image_encoding.astype(int)
# np.savetxt(fname=encodings_write_file, X=str(current_image_encoding), newline=" ")
# with open(encodings_file_path, "w") as text_file:
#     print(str(current_image_encoding), file=text_file)
# for row in current_image_encoding:
#     np.savetxt(encodings_write_file, row)
# encodings_write_file.close()

# print(str(current_image_encoding))
# print(lines)
# quit()

# list = os.listdir(basepath)
# for file in list:
    #     if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
    #         try:
    #             file_path = os.path.join(basepath, file)
    #             saved_image = face_recognition.load_image_file(file_path)
    #             saved_image_encoding = face_recognition.face_encodings(saved_image)[0]

    #             current=current_image_encoding[0]
    #             results = face_recognition.compare_faces([saved_image_encoding], current,  tolerance=0.40)
    #             if(results[0]):
    #                 print(file_path)
    #                 print(results[0])
    #                 counter = 0
    #                 break
    #         except:
    #             continue
    # if counter == 0:
    #     print("Face already registered")
    # else:
    #     print("Face Not Registered")

# files = [f for f in os.listdir('/var/www/html/api_orio/Face_recog_v2/Registered/')]
# print(len(files))
# print(files)

# for f in files:
# current_image = face_recognition.load_image_file(path2)

# userID_image_encoding = face_recognition.face_encodings(userID_image)[0]
# current_image_encoding = face_recognition.face_encodings(current_image)

# if(len(current_image_encoding)>=1):
#     current=current_image_encoding[0]
#     results = face_recognition.compare_faces([userID_image_encoding], current,  tolerance=0.40)
#     print(results[0])
#     #print(face_recognition.face_distance([userID_image_encoding], current))
# else:
#     print("No Face Found")
