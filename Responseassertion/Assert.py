import jmespath
import unittest


class JmespathAssert(unittest.TestCase):

    def assert_element_Exist(self,input, response):
        path = jmespath.search(input, response)
        self.assertIsNotNone(path,':'+input +' dose not exsit in response' )


    def assert_value_Equal(self,input, response, output):
        path = jmespath.search(input, response)
        self.assertEqual(output,path,': the value of {0} is {1}, but expect result is {2} '.format(input,str(path),str(output)))
