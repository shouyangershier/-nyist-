import face_recognition
import numpy as np
from sklearn.externals import joblib


# 进行人脸检测识别并显示
def recognition(rgb_small_frame):

    clf = joblib.load("./model/svm_face.model")

    f = open('./model/name.txt', 'r')
    name_dict = eval(f.read())
    f.close()

    # threshold = 1/(0.75 * len(name_dict))  # 作为阈值进行类别的判断，阈值越大识别出来的越准确，但相对来说就很难识别出来  66.666
    threshold = 0.9

    # 将画面中的人脸进行编码
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        if np.max(clf.predict_proba([face_encoding])) > threshold:
            return name_dict[int(clf.predict([face_encoding]))]
        else:
            return False


if __name__ == '__main__':
    pass

