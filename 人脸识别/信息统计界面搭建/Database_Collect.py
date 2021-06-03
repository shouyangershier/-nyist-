import MySQLdb
import face_recognition



# def Database(image_path, name, team, num, cla, number, teacher):
def Database(account, image_path, name, team, num, cla, number, teacher):  # 新修改内容
    fp = open(image_path,"rb")
    img = fp.read()
    fp.close()
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]  # 将图片转化成编码形式
    face_encoding = face_encoding.tostring()


    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","root","face_registration_system",charset="gbk")

    # 使用cursor() 方法获取操作游标
    cursor = db.cursor()


    # 使用execute方法执行SQL语句
    # cursor.execute("insert into information values(%s,%s,%s,%s,%s,%s,%s,%s) ",(face_encoding,img,name, team, num, cla, number, teacher))
    cursor.execute("insert into stu_information values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(account, face_encoding,img,name, team, num, cla, number, teacher))   # 新修改内容
    # 解决办法：后面的内容虽然是字符串，但是仍然需要加单引号，或者双引号。如我在后面的'%s'上加上了单引号。然后问题就解决了

    db.commit() # 提交
    # 关闭数据库连接
    db.close()
    print("上传成功")


def database_screen_show(account):
    list = []
    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","root","face_registration_system",charset="gbk")

    # 使用cursor() 方法获取操作游标
    cursor = db.cursor()
    cursor.execute("select name,team,num,cla,number,teacher from stu_information where account= %s"% account)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        list.append(row)

    db.close()
    return list

if __name__ == "__main__":
    print(database_screen_show("123"))

    # Database("D:/桌面/python/opencv/image/1.jpg", "谷召振", "仁爱", "1815925182", "软件设计三班", "18837325114", "祝孔涛")
    # Database(1,1,1,1,1,1,1,1)
    pass







