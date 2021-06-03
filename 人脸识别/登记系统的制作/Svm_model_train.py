import os
import face_recognition
import numpy as np
from sklearn import svm
import joblib


# 加载人脸图片并进行编码
def Encode():
    image_path = "./face_database/"
    data_path = "./face_encode/"
    person_list = os.listdir(image_path)
    for person in person_list:
        # if os.path.isfile(data_path + person) is 0:
        if not os.listdir(data_path + person):
            print(image_path + person)
            image_list = os.listdir(image_path + person)
            for i in range(len(image_list)):
                image = image_list[i]
                face = face_recognition.load_image_file(image_path + person + "/" + image)           #  加载人脸图片
                face_locations = face_recognition.face_locations(face)                               #  检测人脸位置
                try:
                    face_enc = face_recognition.face_encodings(face, face_locations)[0]                  #  将人脸特征进行编码
                except:
                    continue
                np.save(data_path + person + "/" + image.split(".")[0], face_enc)

# 训练SVC
def Train_SVC():

    encodings = []
    names = []
    name_dict = {}
    # 加载人脸数据库并学习
    data_path = "./face_encode/"
    person_list = os.listdir(data_path)
    for i, person in enumerate(person_list):
        data_list = os.listdir(data_path + person)
        for data in data_list:
            print(i, data)
            encodings.append(np.load(data_path + person + "/" + data).tolist())
            names.append(int(i))
            name_dict[i] = person

    clf = svm.SVC(C=20, probability=True)
    clf.fit(encodings, names)

    joblib.dump(clf, "./model/svm_face.model")

    f = open('./model/name.txt', 'w')
    f.write(str(name_dict))
    f.close()


if __name__ == '__main__':
    Encode()
    Train_SVC()
    pass
