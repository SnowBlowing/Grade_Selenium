#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/20  18:54
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 持久化存储
# -*- encoding:utf-8 -*-
import pymysql


class Connection:
    conn = None
    db_host = 'localhost'
    db_user = 'root'
    db_psw = '141421'
    db_name = 'grade_selenium'

    def __init__(self):
        try:
            # 链接数据库
            self.conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_psw,
                                        database=self.db_name)
            print("数据库连接成功")
        except pymysql.Error as e:
            print("数据库连接失败" + str(e))

    def close_mysql(self):
        self.conn.close()