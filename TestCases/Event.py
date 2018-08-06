import unittest
from Datacenter.Propertygeter import Property
from ParameterFactory.Parameter import Parameter
from Request.SentRequest import SentRequest
from Request.Basic import Basic

class Event(unittest.TestCase):
    env='staging'
    req=None
    def setUp(self):
        Property(self.env)
        self.env ='staging'
        Parameter.Token = SentRequest(self.env).get_tokens('/utilities/tokens')
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer '+Parameter.Token}
        self.req = SentRequest(Event.env,headers)



