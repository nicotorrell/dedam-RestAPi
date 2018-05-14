from copy import deepcopy
import unittest
import json

import sys
sys.path.append('../database')
from services.database import Database
data = Database()
import app


#BAD_ITEM_URL = '{}/5'.format(BASE_URL)
#GOOD_ITEM_URL = '{}/1'.format(BASE_URL)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_items = deepcopy(data.storage)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_allUsers(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_oneUser(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0]['self'], 'rest/user/1')
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['alias'], 'batman')
        self.assertEqual(data[0]['name'], 'Pepe')
        self.assertEqual(data[0]['surname'], 'Rodriguez')
        self.assertEqual(data[0]['age'], 23)
        self.assertEqual(data[0]['phone'], 632555410)
        self.assertEqual(data[0]['grupo'], {u'href': u'rest/grupo/grupo1', u'name': u'grupo1'})
        self.assertEqual(data[0]['photo'], '541545')

    def test_get_oneUserNotExist(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/3'
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 404)

    def test_get_oneUserEspecifiDataSefl(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/self'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'self': u'rest/user/1'})

    def test_get_oneUserEspecifiDataAlias(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/alias'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'alias': u'batman', u'self': u'rest/user/1/alias'})

    def test_get_oneUserEspecifiDataId(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/id'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'id': 1, u'self': u'rest/user/1/id'})

    def test_get_oneUserEspecifiDataName(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/name'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'name': u'Pepe', u'self': u'rest/user/1/name'})

    def test_get_oneUserEspecifiDataSurName(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/surname'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'surname': u'Rodriguez', u'self': u'rest/user/1/surname'})

    def test_get_oneUserEspecifiDataAge(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/age'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'age': 23, u'self': u'rest/user/1/age'})

    def test_get_oneUserEspecifiDataPhone(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/phone'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'phone': 632555410, u'self': u'rest/user/1/phone'})

    def test_get_oneUserEspecifiDataGrupo(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/grupo'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'grupo': {u'href': u'rest/grupo/grupo1', u'name': u'grupo1'}, u'self': u'rest/user/1/grupo'})

    def test_get_oneUserEspecifiDataPhoto(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/photo'
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'photo': u'541545', u'self': u'rest/user/1/photo'})

    def test_get_oneUserEspecifiDataNoUser(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/3/name'
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 404)

    def test_get_oneUserEspecifiDataFalseData(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/3/coso'
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 404)


    def test_post(self):
        # missing alias and surname
        BASE_URL = 'http://127.0.0.1:5000/rest/user'
        item = {"name": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # missing name and surname
        BASE_URL = 'http://127.0.0.1:5000/rest/user'
        item = {"surname": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # missing alias and name
        BASE_URL = 'http://127.0.0.1:5000/rest/user'
        item = {"surname": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # missing alias, surname and name
        BASE_URL = 'http://127.0.0.1:5000/rest/user'
        item = {"age": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # ok post
        item = {"name": "Moises", "surname": "Martinez", "alias": "Moisy", "age": 27}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data, {u'surname': u'Martinez', u'name': u'Moises', u'self': u'rest/user/3', u'id': 3, u'alias': u'Moisy', u'age': 27})
        # post same alias
        item = {"name": "Moises", "surname": "Ramos", "alias": "Moisy", "id": 3, "age": 27, "self": "rest/user/3"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_updateUserData(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/alias'
        item = {"alias": "Aquaman"}
        response = self.app.put(BASE_URL,
                                data=json.dumps(item),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['alias'], "Aquaman")

    def test_deleteUserData(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1/alias'
        response = self.app.delete(BASE_URL)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data, {u'Succes': u'Element Deleted'})

        URLTEST = 'http://127.0.0.1:5000/rest/user/1/alias'
        response2 = self.app.get(URLTEST)
        self.assertEqual(response2.status_code, 404)

    def test_deleteUser(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/user/1'
        response = self.app.delete(BASE_URL)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data, {u'Succes': u'Element Deleted'})

        URLTEST = 'http://127.0.0.1:5000/rest/user/1'
        response2 = self.app.get(URLTEST)
        self.assertEqual(response2.status_code, 404)

    def test_getGrupos(self):
        BASE_URL = 'http://127.0.0.1:5000/rest/grupo'
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(len(data), 2)

    def test_postGrupo(self):
        #no name
        BASE_URL = 'http://127.0.0.1:5000/rest/grupo'
        item = {"surname": "Moises"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # ok post
        BASE_URL = 'http://127.0.0.1:5000/rest/grupo'
        item = {"name": "Admin"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(item),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data, {u'self': u'rest/group/Admin', u'name': u'Admin'})

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items


if __name__ == "__main__":
    unittest.main()