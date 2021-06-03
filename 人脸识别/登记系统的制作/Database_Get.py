import MySQLdb
import numpy as np


class DatabaseGet():
    def __init__(self):
        # 打开数据库连接
        self.db = MySQLdb.connect("localhost", "root", "root", "face_registration_system", charset="gbk")

        # 使用cursor() 方法获取操作游标
        self.cursor = self.db.cursor()
        pass

    def database_get_encode(self):
        known_face_encodings = []
        num_list = []
        # 使用execute方法执行SQL语句
        self.cursor.execute("select encode,num from stu_information")

        while True:
            row = self.cursor.fetchone()
            if not row:
                break
            feature = np.frombuffer(row[0], dtype=np.float64)
            known_face_encodings.append(feature)
            num_list.append(row[1])
        # 关闭数据库连接
        # self.db.close()
        return known_face_encodings,num_list

    def database_get_other(self,num_matching):
        self.cursor.execute("select image,name,team,cla,number,teacher from stu_information where num = %s" % num_matching)
        row = self.cursor.fetchone()
        self.image = row[0]
        self.name = row[1]
        self.team = row[2]
        self.cla = row[3]
        self.number = row[4]
        self.teacher = row[5]
        # 关闭数据库连接
        # self.db.close()
        return self.image,self.name, self.team, self.cla, self.number, self.teacher

    def database_get_image(self):
        images = []
        nums = []
        # 使用execute方法执行SQL语句
        self.cursor.execute("select image,num from stu_information")

        while True:
            row = self.cursor.fetchone()
            if not row:
                break
            images.append(row[0])
            nums.append(row[1])

        # 关闭数据库连接
        # self.db.close()
        return images,nums

if __name__ == "__main__":
    database = DatabaseGet()
    # database.database_get_num()
    image = database.database_get_image()
    # image = database.database_get_encode()
    print(image[0])
    # while True:
    #     x = int(input("请输入："))
    #     num1 = "1815925182"
    #     if x == 1:
    #         database.database_get_other(num1)
    #     else:
    #         continue