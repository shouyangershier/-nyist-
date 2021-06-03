from PyQt5.Qt import *
from resource.login import Ui_Form
class LoginPane(QWidget, Ui_Form):

    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True) # 使背景图片得到显示
        self.setupUi(self)
        movie = QMovie(":/login/images/login_top.gif")

        movie.setScaledSize(QSize(500,232))
        self.login_top_bg_label.setMovie(movie)
        movie.start()
    def show_register_pane(self):
        self.show_register_pane_signal.emit()

    def open_qq_link(self):
        # 通过点击二维码，加入qq群聊
        link = "http://shang.qq.com/wpa/qunwpa?idkey=8f289c6676ea1c13ef82c6389ccbe8b3dc4afc20f394e88668eb4920b9215cab"
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        if len(account) > 0 and len(pwd) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_signal.emit(account, pwd)

    def auto_login(self, checked):
        if checked:
            self.remember_pwd_cb.setChecked(True)

    def remember_pwd(self, checked):
        if not checked:
            self.auto_login_cb.setChecked(False)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())
        animation.setDuration(100)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = LoginPane()

    window.show()

    sys.exit(app.exec_())















