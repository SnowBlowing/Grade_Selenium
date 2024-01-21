#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 224/1/21  16:5
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import sqlite3


class SQL:
    def __init__(self):
        self.conn = sqlite3.connect('student_grade.db')  # 链接数据库
        self.cursor = None  # 游标对象
        self.results = None  # 查询结果
        self.cursor = self.conn.cursor() # 创建游标对象
        self.create_table()  # 创建grade表

    # 创建表
    def create_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS grade  (
              'name' TEXT NULL DEFAULT '?',
              exam_id TEXT NULL DEFAULT '?',
              idcard TEXT NULL DEFAULT '?',
              chinese TEXT NULL DEFAULT '?',
              math TEXT NULL DEFAULT '?',
              english TEXT NULL DEFAULT '?',
              physics TEXT NULL DEFAULT '?',
              chemistry TEXT NULL DEFAULT '?',
              political TEXT NULL DEFAULT '?',
              history TEXT NULL DEFAULT '?',
              geography TEXT NULL DEFAULT '?',
              biology TEXT NULL DEFAULT '?',
              level_pol TEXT NULL DEFAULT '?',
              level_his TEXT NULL DEFAULT '?',
              level_physics TEXT NULL DEFAULT '?',
              level_chem TEXT NULL DEFAULT '?',
              level_geo TEXT NULL DEFAULT '?',
              level_bio TEXT NULL DEFAULT '?',
              physical TEXT NULL DEFAULT '?',
              comprehensive TEXT NULL DEFAULT '?',
              experiment TEXT NULL DEFAULT '?',
              music_art TEXT NULL DEFAULT '?',
              total TEXT NULL DEFAULT '?'
            )
            '''
        )

    def insert_grade(self, student):
        # 插入数据
        self.cursor.execute(
            '''
                INSERT INTO grade (chinese, math, english, physics, chemistry, political, history, geography, biology, 
                level_pol, level_his, level_physics, level_chem, level_geo, level_bio, physical, comprehensive,
                experiment, music_art, total) 
                VALUES (
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT),
                    COALESCE(?, DEFAULT)
                )
            '''
            , (student.chinese, student.math, student.english, student.physics, student.chemistry, student.political,
               student.history, student.geography, student.biology, student.level_pol, student.level_his,
               student.level_physics, student.level_chem, student.level_geo, student.level_bio, student.physical,
               student.comprehensive, student.experiment, student.music_art, student.total)
        )

    # 提交事务
    def commit(self):
        self.conn.commit()

    def select_grade(self):
        # 查询数据
        self.cursor.execute('SELECT * FROM grade')
        # 获取查询结果
        self.results = self.cursor.fetchall()

        # 遍历每一行并拆分数据
        # chinese = row[0]
        # math = row[1]
        # english = row[2]
        # physics = row[3]
        # chemistry = row[4]
        # political = row[5]
        # history = row[6]
        # geography = row[7]
        # biology = row[8]
        # level_pol = row[9]
        # level_his = row[10]
        # level_physics = row[11]
        # level_chem = row[12]
        # level_geo = row[13]
        # level_bio = row[14]
        # physical = row[15]
        # comprehensive = row[16]
        # experiment = row[17]
        # music_art = row[18]
        # total = row[19]

    # 关闭连接
    def close_connection(self):
        self.conn.close()
