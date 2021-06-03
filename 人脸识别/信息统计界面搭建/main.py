from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from Collect_Pane import CollectPane
from Manage_Pane import ManagePane
import Database_Collect
import Database_Account


from PyQt5.Qt import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login_pane = LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    collect_pane = CollectPane()
    register_pane.show()
    manage_pane = ManagePane(collect_pane)
    manage_pane.move(1200,0)    # 246 0
    manage_pane.show()



    # 槽函数
    def exit_register_pane():
        # 退出的动画制作
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def show_reister_pane():

        # 弹出的动画制作
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0,450))# register_pane.pos() 获取当前窗口位置
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def check_login(account, pwd):
        # 随后连接诶数据库
        try:
            password = Database_Account.user_account_matching(account)
            if password == pwd:
                collect_pane.accept(account)         #   新添加内容
                collect_pane.show()
                login_pane.hide()
                print("登陆成功")
            else:
                login_pane.show_error_animation()
        except:
            login_pane.show_error_animation()
    def stu_data_uploading(image_path, name, team, num, cla, number, teacher):
        account = collect_pane.ret()
        try:
            # Database_Collect.Database(image_path, name, team, num, cla, number, teacher)
            Database_Collect.Database(account, image_path, name, team, num, cla, number, teacher)   # 新修改内容
        except:
            collect_pane.hint(False)
        else:
            collect_pane.hint(True)
    def user_account_uploading(account, pwd):
        try:
            Database_Account.user_account_save(account,pwd)
        except:
            # 此处也要连接注册界面-标注出注册账号失败
            register_pane.hint(False)
        else:
            #  此处连接注册界面-标注出注册账号成功
            register_pane.hint(True)
    def collect_btn():
        manage_pane.move(1200, 0)# 移至窗口外，以隐藏窗口



    def manage_btn():
        manage_pane.move(246, 0)
        manage_pane.stu_show(collect_pane)



    # 信号连接
    register_pane.exit_signal.connect(exit_register_pane)
    register_pane.register_account_pwd_signal.connect(user_account_uploading) # 随后存入数据库进行保存
    login_pane.show_register_pane_signal.connect(show_reister_pane)
    login_pane.check_login_signal.connect(check_login) # 随后调出数据库中的信息进行验证
    collect_pane.uploading_checked.connect(stu_data_uploading)
    collect_pane.collect_btn_checked.connect(collect_btn)
    collect_pane.manage_btn_checked.connect(manage_btn)

    login_pane.show()

    sys.exit(app.exec_())
























