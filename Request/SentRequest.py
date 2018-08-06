from Request.Basic import Basic
from Config.Config import Config
from Datacenter.Propertygeter import Property

class SentRequest(Basic):
    sessionid=0
    def __init__(self,env='qa',headers=None):
        Basic(headers)
        self.url=Config(env).get_property('url')
        self.sessionid=Property(env).get_sessionid()
    def get_tokens(self,tokenurl):
        tokens= self.post_without_header_body(self.url+tokenurl)
        return tokens['access_token']

    def getResp(self,pathurl):
        response=self.get(self.url+pathurl)
        return response

