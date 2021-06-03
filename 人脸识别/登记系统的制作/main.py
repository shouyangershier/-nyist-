from Recognition_Pane import RecognitionPane
from Face_Recognition import FaceRecognition
from Database_Get import DatabaseGet
import Data_to_enhance
import Svm_model_train
from PyQt5.Qt import *
import sys


if __name__ == '__main__':
    index = Data_to_enhance.start()
    # 如果 index 不等于空，也就是说数据库中添加了新的数据
    if index != []:
        Svm_model_train.Encode()
        Svm_model_train.Train_SVC()

    app = QApplication(sys.argv)
    recogintion_pane = RecognitionPane()
    face_recognition = FaceRecognition()
    database_get = DatabaseGet()
    recogintion_pane.show()

    # ---------------- 功能一------------------
    # 与人脸识别程序连接，识别匹配人脸信息
    # 从数据库中得到匹配的数据，然后传过来，在通过这个传递个登记系统的界面
    known_face,num_list = database_get.database_get_encode()
    def matching(flag,image):
        num_matching = face_recognition.kernel(image,known_face,num_list)
        if num_matching:
            recogintion_pane.show_information(num_matching)

    recogintion_pane.camera_image.connect(matching)

    # ----------------------------------

    sys.exit(app.exec_())

