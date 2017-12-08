import pymysql

class Wang_Mysql():
    def __init__(self):
        #数据库连接信息
        self.connection = pymysql.connect(
            host="hiiso.xicp.cn",
            port = 33060,
            user = "happy",
            password = "happy",
            db = "happy"
        )
        #使用cursor()方法获取操作游标
        self.cursor = self.connection.cursor()

    def select(self,sql):
        #SQL查询语句
        self.cursor.execute(sql)
        #查询数据库单条数据
        result = self.cursor.fetchone()
        return result

    def selects(self,sql):
        self.cursor.execute(sql)
        #查询数据库多条数据
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    #测试代码
    sql = "select * from t_user where id > 200"
    results = Wang_Mysql().selects(sql)
    print(len(results))
    for result in results:
        print(result)


