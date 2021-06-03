import face_recognition
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import pickle
import cv2
import os
import Svm_face_recognition

class FaceRecognition():
    def __init__(self):
        self.process_this_frame = True
        self.label = "fake"
        # 加载人脸检测模型和活体模型
        self.protoPath = os.path.sep.join(["face_detector", "deploy.prototxt"])  # 路径组合
        self.modelPath = os.path.sep.join(["face_detector","res10_300x300_ssd_iter_140000.caffemodel"])
        self.net = cv2.dnn.readNetFromCaffe(self.protoPath, self.modelPath)  # 用于进行SSD网络的caffe框架的加载，（进行目标检测的网络）
        self.model = load_model("./model/liveness.model")  # liveness.model   :   keras 训练好的模型
        self.le = pickle.loads(open("./model/le.pickle", "rb").read())  # le.pickle        :   类别标签编码器


    def kernel(self, frame, known_face,num_list):
        self.label = "fake"
        # 改变摄像头图像的大小，图像小，所做的计算就少
        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))  # 对图像进行归一化操作(-1, 1)
        # pass the blob through the network and obtain the detections and
        # predictions
        self.net.setInput(blob)  # 表示将图片输入到caffe网络中
        detections = self.net.forward()  # 输出前向传播的预测结果

        # 对探测结果进行循环
        for i in range(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections  过滤掉微弱的检测信号
            if confidence > 0.8:
                # compute the (x, y)-coordinates of the bounding box for
                # the face and extract the face ROI
                # 计算出人脸的坐标范围
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = face_box = box.astype("int")
                startX = max(0, startX)
                startY = max(0, startY)
                endX = min(w, endX)
                endY = min(h, endY)
                if startX > 1200 or startY > 1200 or endX > 1200 or endY > 1200:
                    break
                face = frame[startY:endY, startX:endX]
                face = cv2.resize(face, (32, 32))
                face = face.astype("float") / 255.0
                face = img_to_array(face)          # 将人脸矩阵中的整数，换成浮点数
                face = np.expand_dims(face, axis=0) # 在 0 轴上，添加一个维度
                preds = self.model.predict(face)[0]
                j = np.argmax(preds)  # 取出 preds 中最大的数的索引
                if preds[j] > 0.2:
                    self.label = self.le.classes_[j]


        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # opencv的图像是BGR格式的，而我们需要的是RGB格式，因 此要进行一个转换
        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            # 根据encoding来判断是不是同一个人，是就输出true,不是为false
            if str(self.label) == "real":
                num = Svm_face_recognition.recognition(rgb_small_frame)
                return num




if __name__ == "__main__":
    pass



