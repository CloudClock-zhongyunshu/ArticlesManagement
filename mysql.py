import pymysql  # 引入pymysql模块
import traceback  # 引入python中的traceback模块，跟踪错误
import sys  # 引入sys模块


class MysqlUtil:
    def __init__(self):
        # 初始化方法，连接数据库
        host = '127.0.0.1'  # 主机名
        user = 'root'  # 数据库用户名
        password = '37425KxeBi@.cn'  # 数据库密码
        database = 'database_test'  # 数据库名称
        self.db = pymysql.connect(host=host, user=user, password=password, db=database)  # 建立连接
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)  # 设置游标，并将游标设置为字典类型

    # 添加数据（用户注册、添加笔记）
    def insert(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # 如果发生异常，则回滚
            print("发生异常", e)
            self.db.rollback()
        finally:
            # 关闭数据库连接
            self.db.close()

    # 查询数据库：单个结果集
    def fetchone(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except:
            # 输出异常信息
            traceback.print_exc()
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 关闭数据库连接
            self.db.close()
        return result

    # 查询数据库：多个结果集
    def fetchall(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            # 采用sys模块回溯最后的异常
            info = sys.exc_info()
            print(info[0], ":", info[1])
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 关闭数据库连接
            self.db.close()
        return results

    #  删除结果集
    def delete(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 将错误日志输入到目录文件中
            f = open("\log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 关闭数据库连接
            self.db.close()

    # 更新结果集
    def update(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 关闭数据库连接
            self.db.close()
