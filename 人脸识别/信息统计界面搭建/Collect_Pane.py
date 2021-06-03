from PyQt5.Qt import *
from PyQt5 import QtGui
from resource.collect import Ui_Form
import numpy as np


class CollectPane(QWidget,Ui_Form):
    uploading_checked = pyqtSignal(str,str,str,str,str,str,str)
    collect_btn_checked = pyqtSignal()
    manage_btn_checked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.account = ""
        self.setAttribute(Qt.WA_StyledBackground, True) # 使背景图片得到显示
        self.setupUi(self)

    def uploading(self):
        name = self.name_line.text()
        team = self.team_line.currentText()
        num = self.num_line.text()
        cla = self.class_line.text()
        number = self.number_line.text()
        teacher = self.teacher_line.text()
        self.uploading_checked.emit(self.imgName, name, team, num, cla, number, teacher)

    def enable_inf_btn(self):
        name = self.name_line.text()
        team = self.team_line.currentText()
        num = self.num_line.text()
        cla = self.class_line.text()
        number = self.number_line.text()
        teacher = self.teacher_line.text()
        if len(name) > 0 and len(team) > 0 and len(num) > 0 and len(cla) > 0 and len(number) > 0 and len(teacher) > 0:
            self.uploading_btn.setEnabled(True)
        else:
            self.uploading_btn.setEnabled(False)


    def openimage(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.imgName).scaled(self.image_label.width(), self.image_label.height())
        self.image_label.setPixmap(jpg)

    def hint(self,Bool):
        if Bool:
            self.label_hint.setText("上传成功")
        else:
            self.label_hint.setText("上传失败")

    def collect_btn(self):
        self.collect_btn_checked.emit()
        pass
    def manage_btn(self):
        self.manage_btn_checked.emit()
        pass

    def accept(self,account):
        # 接收账号数据
        self.account = account
    def ret(self):
        # 返回账号数据
        return self.account

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = CollectPane()
    window.show()

    sys.exit(app.exec_())

