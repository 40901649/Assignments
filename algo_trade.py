"""
DocString
"""

import re
Master_list = {}

class Traders:
    """
    docString
    """
    def __init__(self, name, pwd = 'abcd'):
        self.name = name
        self.pwd = pwd
        Master_list[self.name] = self.pwd

class Login:
    """
    DocString
    """
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        try:
            assert re.match(pwd, Master_list[name])
            print(f"{self.name} login is successful! Enjoy the trading!")
        except AssertionError:
            print(f"{self.name} login is not successful! Please try again!")

Member1 = Traders('Ravi', 'asdf')
Member2 = Traders('Shanvi')
print(Member1.__dict__)
print(Member2.__dict__)
print(Master_list)

Memberlogin1 = Login('Shanvi','abcd')
Memberlogin2 = Login('Ravi', 'asdf1')
