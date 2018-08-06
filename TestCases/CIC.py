import unittest
from TestCases.Event import Event
from Responseassertion.Assert import JmespathAssert

class TestCIC(Event):

    def setUp(self):
        Event.setUp(self)
        self.JmespathAssert=JmespathAssert()

    def test_session_cic(self):
        url='/sessions/{0}/cic?language={1}'.format(self.req.sessionid,'en-US')
        response=self.req.getResp(url)
        self.JmespathAssert.assert_element_Exist('cii',response)

    def test_session_cic_sessionid(self):
        url='/sessions/{0}/cic?language={1}'.format(self.req.sessionid,'en-US')
        response=self.req.getResp(url)
        self.JmespathAssert.assert_value_Equal('sessionId',response,self.req.sessionid)

if __name__ == '__main__':
    unittest.main()