import pymysql

from utils.log_util import logger
from utils.read_data import base_data

data = base_data.read_ini()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}


class MySqlDb:
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 选择一条sql
    def select_db_one(self, sql):
        logger.info(f"执行SQL:{sql}")
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 选择多条sql
    def select_db_all(self, sql):
        logger.info(f"执行SQL:{sql}")
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute_db(self, sql):
        try:
            logger.info(f"执行SQL:{sql}")
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行SQL出错了{}" + format(e))
        return self.cur.fetchall()


if __name__ == '__main__':
    db = MySqlDb()
    r = db.select_db("SELECT * FROM `dl`.`dl_operate_area`")
    print(r)
