import pymssql


class MSSQL:

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        Get connect information
        Return: conn.cursor()
        """
        if not self.db:
            raise(NameError,"No DB information")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"Connect to DB error")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        Excute query
        Return:list(tuple)

        Example：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        Excute Nonquery

        Example：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

# def main():
# ## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
# ## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")
#
# #connection = pymssql.connect('Server=CNE1QAOMNIDB01.e1ef.com;Database=OmniOperation;uid=sa;pwd=P@ssw@rd1')
#
#     ms = MSSQL(host="CNE1QAOMNIDB01.e1ef.com",user="sa",pwd="P@ssw@rd1",db="OmniOperation")
#     members = ms.ExecQuery("SELECT TOP 1 * FROM [dbo].[Group]")
#     for member in members:
#         print (member)
#
# if __name__ == '__main__':
#     main()