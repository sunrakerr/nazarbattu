import os
import time
import cv2
import face_recognition as fr
import pyrebase
import datetime
import pickle
import numpy as np
from firebase import firebase
from darkflow.net.build import TFNet
options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}

tfnet = TFNet(options)

#setup firebase
fb = firebase.FirebaseApplication('https://facein-396b4.firebaseio.com/', None)
config={
    '''
    firebase creds. and api key goes here
    '''
}
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

folder=" " #json out folder
#camcode="python flow --model cfg/yolo.cfg --load bin/yolo.weights --demo camera --gpu 1.0"
getjson="python flow --imgdir {}/ --model cfg/yolo.cfg --load bin/yolo.weights --json".format(folder)

jsonfolder = folder+"/out/"

date=datetime.datetime.now()
date=str(date).split()[0]
os.system(getjson)



def get_encoded_faces():
    """
    returns encoding of images from encoded pkl
    """
    with open('encoded.pkl', 'rb') as f:
        newencode=pickle.load(f)
    return newencode

def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
  
    face_locations = fr.face_locations(img)
    faceno=len(face_locations)
    print("faceno:",faceno)
    unknown_face_encodings = fr.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = fr.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = fr.face_distance(faces_encoded, face_encoding)
 
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
    return [faceno,face_names]

while True:
    for filename in os.listdir(folder):
        time.sleep(1)
        if filename.endswith("jpg") or filename.endswith("png"):
            imgcv = cv2.imread(folder+"/"+filename)
            print(filename)

            result=tfnet.return_predict(imgcv)
            print(result)
            if len(result)==0:
                print("res is empty")

            for object in result:
             
                if object["label"] == "person":
                    real_image=filename.split(".")[0]
                    imgjpg=real_image+".jpg"
                    print("real img:",imgjpg)

                    #img got
                    faceno,persons =classify_face(folder+"/"+imgjpg)
                    print("no of faces",faceno)
                    print(persons)
                    persons_up=",".join(persons)
                    if persons_up=="":
                        persons_up="Unrecognized"
                    print(persons_up)
                    # save to firebase
                    try:
                        cloudpath = "cam_images/{}".format(imgjpg)
                        localpath = folder + "/" + imgjpg
                        storage.child(cloudpath).put(localpath)

                        fb.put("dates/{}/{}".format(date,real_image),"pcount", faceno)
                        fb.put("dates/{}/{}".format(date,real_image),"pname", persons_up)
                    except:
                        print("firebase error")
                    break

            os.remove(folder+"/"+filename)
    print("waiting")