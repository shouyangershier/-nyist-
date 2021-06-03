from PyQt5.Qt import *
from resource.register import Ui_Form


class RegisterPane(QWidget, Ui_Form):

    exit_signal = pyqtSignal() # 退出信号
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True) # 使背景图片得到显示
        self.setupUi(self)
        self.animation_targets = [self.about_menue_btn, self.reset_menue_btn, self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menue(self, checked):

        # 创建一个序列动画组（产生陆续的动画）
        animation_group = QSequentialAnimationGroup(self)
        for idx,target in enumerate(self.animation_targets):
            # 创建动画对象
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
            else:
                animation.setEndValue(self.main_menue_btn.pos())
                animation.setStartValue(self.animation_targets_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce) # 设置弹簧效果
            animation_group.addAnimation(animation)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        """
        if not checked:
            # 创建一个序列动画组（产生陆续的动画）
            animation_group = QSequentialAnimationGroup(self)
            for idx,target in enumerate(self.animation_targets):
                # 创建动画对象
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b"pos")
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
                animation.setDuration(200)
                animation.setEasingCurve(QEasingCurve.InOutBounce) # 设置弹簧效果
                animation_group.addAnimation(animation)

            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        else:
            # 创建一个序列动画组（产生陆续的动画）
            animation_group = QSequentialAnimationGroup(self)
            for idx,target in enumerate(self.animation_targets):
                # 创建动画对象
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b"pos")
                animation.setEndValue(self.main_menue_btn.pos())
                animation.setStartValue(self.animation_targets_pos[idx])
                animation.setDuration(200)
                animation.setEasingCurve(QEasingCurve.InOutBounce) # 设置弹簧效果
                animation_group.addAnimation(animation)

            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        """

    def about(self):
        QMessageBox.about(self,"软件提示","本系统由软件学院仁爱社团提供技术支持")
        pass
    def reset(self):
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()
        pass

    def exit_pane(self):
        # 当点击退出按钮后，将退出信号传递出去，跳回调用的界面
        self.exit_signal.emit()
        pass
    def check_register(self):
        # 注册按钮点击后，将账号和密码传递出去
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        self.register_account_pwd_signal.emit(account_txt, password_txt)
        pass
    def enable_register_btn(self):
        # 对文本框输入的内容进行监控
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        cp_txt = self.confirm_pwd_le.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(cp_txt)>0 and password_txt == cp_txt:
            self.register_btn.setEnabled(True) # 设置按钮可用
        else:
            self.register_btn.setEnabled(False)

    def hint(self,Bool):
        # 当用户注册时，判断是否注册成功
        if Bool:
            self.label_hint.setText("注册成功")
        else:
            self.label_hint.setText("注册失败")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = RegisterPane()

    # 通过类对象调用内部属性传递出来的信号对数据进行操作
    window.exit_signal.connect(lambda : print("退出"))
    window.register_account_pwd_signal.connect(lambda a,p:print(a,p))

    window.show()

    sys.exit(app.exec_())














