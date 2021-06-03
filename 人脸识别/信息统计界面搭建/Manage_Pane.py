from PyQt5.Qt import *
from resource.manage import Ui_Form
from PyQt5 import QtCore
import Database_Collect
from Collect_Pane import CollectPane

class ManagePane(QWidget,Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True) # 使背景图片得到显示
        self.setupUi(self)
        self.collect_pane = CollectPane()


    def stu_show(self,collect_pane):
        account = collect_pane.ret()
        list = Database_Collect.database_screen_show(account)

        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(len(list))
        tablewidget.setColumnCount(6)

        layout.addWidget(tablewidget)

        # 设置表头
        tablewidget.setHorizontalHeaderLabels(['姓名', '社团', '学号',"班级","电话","辅导员"])

        for i in range(len(list)):
            k = 0
            for j in list[i]:
                Item = QTableWidgetItem(j)
                tablewidget.setItem(i, k, Item)
                # print(i, k, j)
                k += 1

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # # 调整单元格到适合内容的大小
        tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive | QHeaderView.Stretch)
        # tablewidget.resizeColumnsToContents()
        # tablewidget.resizeRowsToContents()
        # 设置滚动条
        tablewidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setLayout(layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = ManagePane()
    window.show()

    sys.exit(app.exec_())
    pass