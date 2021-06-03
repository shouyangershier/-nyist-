import MySQLdb



def user_account_save(account, password):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "face_registration_system", charset="gbk")

    # 使用cursor() 方法获取操作游标

    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("insert into user values(%s,%s)",(account, password))

    db.commit() # 提交
    # 关闭数据库连接
    db.close()

def user_account_matching(account):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "face_registration_system", charset="gbk")

    # 使用cursor() 方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("select password from user where account = %s" % account)
    row = cursor.fetchone()

    # 关闭数据库连接
    db.close()
    return row[0]

if __name__ == "__main__":
    # user_account_matching("123")

    # print(account)
    pass