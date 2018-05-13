
import unittest
import sys
sys.path.append('../services')

from services.service import Server


def moked_request():
    request = {}
    request['username'] = "Eduard"
    request['email'] = "edu@mail.com"
    return request


class AppTest(unittest.TestCase):
    def setUp(self):
        self.database = FakeDataBase()

    def test_adduser(self):
        service = Server(self.database)
        request = moked_request()
        return_value = service.add_user(request)
        self.assertEqual("correctly_added", return_value)
        self.assertEqual("Eduard", self.database.added_username)
        self.assertEqual("edu@mail.com", self.database.added_mail)


class FakeDataBase:
    def __init__(self):
        self.added_username = ''
        self.added_mail = ''

    def add_user(self, username, mail):
        self.added_username = username
        self.added_mail = mail
        return "correctly_added"

