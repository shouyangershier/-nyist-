from PyQt5.Qt import *
from PyQt5 import QtCore,QtWidgets,QtGui
import cv2
import csv
import numpy
import datetime
from resource.recognition_sys import Ui_Form
from Database_Get import DatabaseGet

class RecognitionPane(QWidget,Ui_Form):
    camera_image = pyqtSignal(bool, numpy.ndarray)
    # confirm_inf = pyqtSignal(bool)
    def __init__(self):
        self.database_get = DatabaseGet()
        self.rec = True # 是否需要进行识别，默认不是被
        # self.btn_clicked = False
        super().__init__()
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.setAttribute(Qt.WA_StyledBackground, True)  # 使背景图片得到显示
        self.setupUi(self)
        self.timer_camera.timeout.connect(self.show_camera)

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False: # 如果定时器没有启动过，则启动定时器开始录像
            flag = self.cap.open(self.CAM_NUM)
            if flag == False: # 当摄像头没有打开成功
                msg = QtWidgets.QMessageBox.warning(self,'warning',"请检查设备摄像装置是否出错",buttons = QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30) # 打开定时器，每30毫秒从摄像头中提取一帧图像
                self.button_open_camera.setText("关闭摄像头")

        else:
            self.timer_camera.stop() #  如果定时器已经启动，则当再次按下开关时关闭定时器
            self.cap.release() # 释放视频流
            self.label_show_camera.clear() # 清空摄像显示区域
            self.button_open_camera.setText("打开摄像头")

    def show_camera(self):
        # 将记录过的摄像显示在 QLabel中
        flag, self.image = self.cap.read() # 读取摄像
        show = cv2.resize(self.image,(400,500))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB) # 将摄像色彩跳回RGB，才可显示真实颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888) # 把读取到的视频数据变成 QImage形式
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage)) # 显示摄像

        if self.rec:
            self.camera_image.emit(flag, self.image)  # 将该信号发射出去

        # self.camera_image.emit() # 将该信号发射出去

    def empty(self):
        self.picture_label.clear()
        self.name_lineEdit.clear()
        self.team_lineEdit.clear()
        self.num_lineEdit.clear()
        self.class_lineEdit.clear()
        self.number_lineEdit.clear()
        self.teacher_lineEdit.clear()

    def retry(self):
        self.empty()
        self.rec = True

    def save(self):
        # 并当用户点击确认按钮后，将匹配到的数据传递给某个表格文件，记录下来
        # 如果用户点击了重试按钮，则不在记录该数据
        curr_time = datetime.datetime.now()
        time_str = curr_time.strftime("%Y-%m-%d %H:%M:%S")
        data = [time_str,self.name,self.team, self.num, self.cla, self.number, self.teacher]
        # 1. 创建文件对象
        f = open('information.csv', 'a+', encoding='utf-8')
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
        # 5. 关闭文件
        f.close()

    def confirm(self):
        self.empty()
        self.rec = True
        self.save()


    # def show_information(self,image,name,team,num,cla,number,teacher):
    def show_information(self,num_matching):
        image, self.name, self.team, self.cla, self.number, self.teacher = self.database_get.database_get_other(num_matching)
        self.num = num_matching

        fout = open('./image/image.jpg', 'wb')
        fout.write(image)
        fout.close()
        img = QPixmap('./image/image.jpg')
        self.picture_label.setPixmap(img)
        self.picture_label.setScaledContents(True)
        self.name_lineEdit.setText(self.name)
        self.team_lineEdit.setText(self.team)
        self.num_lineEdit.setText(num_matching)
        self.class_lineEdit.setText(self.cla)
        self.number_lineEdit.setText(self.number)
        self.teacher_lineEdit.setText(self.teacher)
        # self.signalling(False)
        self.rec = False

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = RecognitionPane()
    window.show()

    sys.exit(app.exec_())

