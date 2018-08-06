from Datacenter.DBreader import MSSQL
from Config.Config import Config

class Property:

    def __init__(self,env):
        config=Config(env)
        self.ms = MSSQL(host=config.get_property("host"),user=config.get_property('user'),pwd=config.get_property('pwd'),db=config.get_property('db'))

    def get_groupid(self):
        sql='SELECT TOP 1 id FROM [dbo].[Group]'
        group=self.ms.ExecQuery(sql)
        return group[0][0]

    def get_sessionid(self):
        sql='SELECT TOP 1 sessionId,* FROM [OmniOperation].[dbo].[CICResult] where status=1 order by 1 desc'
        sessionid=self.ms.ExecQuery(sql)
        return sessionid[0][0]
# def main():
#    print(Property().get_groupid())
#    print(Property().get_sessionid())
#
# if __name__ == '__main__':
#     main()