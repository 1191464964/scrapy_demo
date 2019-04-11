import pymysql
import pymysql.cursors


class DButil:
    def __init__(self):
        self.conn = self.connect1()

    # 连接网络数据库（把connect1改成connect）
    def connect(self):
        config = {
            'host': '192.168.10.114',
            'port': 3306,
            'user': 'test',
            'password': 'test',
            'db': 'crawler_100',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,  # 返回字典(dict)表示的记录
        }
        conn = pymysql.connect(**config)
        return conn

    def connect1(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'db': 'test2',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,  # 返回字典(dict)表示的记录
        }
        conn = pymysql.connect(**config)
        return conn

    # 关闭mysql连接
    def close_mysql(self):
        self.conn.close()

    def setstatus(self, tbname, id):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute('update ' + tbname + ' set type=%s where id=%s', (1, id))
            conn.commit()
        except Exception as e:
            print("设置任务状态失败,原因：%s" % e)

    def getnum(self, tablename):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute('select count(*) from ' + tablename)
            result = cur.fetchone()
            return result["count(*)"]
        except Exception as e:
            print("查询失败,原因：%s" % e)

    def runsql(self, sql):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print("查询失败,原因：%s" % e)

    def geturl(self, tablename):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute('select id,url from ' + tablename)
            result = cur.fetchall()
            return result
        except Exception as e:
            print("查询失败,原因：%s" % e)
        finally:
            self.close_mysql()

    # 以字典形式存入数据库
    def insert_fun(self, tbname, item):
        newData = {}
        conn = self.conn
        cur = conn.cursor()
        for key in item:
            if item[key] == None:
                item[key] = ""
            else:
                item[key] = str(item[key]).replace("\'", "\"")
            newData[key] = "'" + item[key] + "'"
        key = ','.join(newData.keys())
        value = ','.join(newData.values())
        sql = "insert into " + tbname + "(" + key + ") values(" + value + ")"
        try:
            cur.execute(sql)
            conn.commit()
            print("数据值存入数据库成功")
            return 1
        except Exception as e:
            print("语句出错{}".format(sql))
            print(e)
            return 0
            # finally:
            #     self.close_mysql()

    def exist_url(self, tbname, url):
        conn = self.conn
        cur = conn.cursor()
        sql = "select * from " + tbname + " where url=%s"
        try:
            rests = cur.execute(sql, url)
            if rests:
                return True
        except Exception as e:
            print("查询表%s的url失败,原因：%s" % (tbname, e))
        return False

    def find_all(self, tablename):
        conn = self.conn
        cur = conn.cursor()
        try:
            # sql='select * from '+ tablename+' where status = 0 LIMIT 0, 1000'
            sql = 'select * from ' + tablename + ' where type = 0'
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print("查询失败,原因：%s" % e)

    def save_mysql(self, table_name, item):
        # table_name = 'middle_banyuetan'
        if self.exist_url(table_name, item["url"]):
            print("重复1次")
        else:
            self.insert_fun(table_name, item)

    def save_body(self, table_name, table_url, item, id):
        if self.insert_fun(table_name, item):
            self.setstatus(table_url, id)
        else:
            self.setstatus(table_url, id)

    def failed_status(self, tbname, id):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute('update ' + tbname + ' set type=%s where id=%s', (2, id))
            conn.commit()
        except Exception as e:
            print("设置任务状态失败,原因：%s" % e)


if __name__ == '__main__':
    db = DButil()
    a = db.geturl("baidu_068")
    for m in a:
        print(m)
        # print(a)
        # print(b)
        # a.updatestatus(3,5,1000)
