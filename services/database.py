from flask import jsonify, abort, make_response
import json

class Database:

    def __init__(self):
        self.storage = [
            {
                'self': 'rest/user/1',
                'id': 1,
                'alias': 'batman',
                'name': 'Pepe',
                'surname': 'Rodriguez',
                'age': 23,
                'phone': 632555410,
                'grupo':
                    {
                        'name': 'grupo1',
                        'href': 'rest/grupo/grupo1'
                    },
                'photo': '541545'
            },
            {
                'self': 'rest/user/2',
                'id': 2,
                'alias': 'superman',
                'name': 'Juan',
                'surname': 'Sanchez',
                'age': 26,
                'phone': 632598147,
                'grupo':
                    {
                        'name': 'grupo2',
                        'href': 'rest/grupo/grupo2'
                    },
                'photo': '123456'
            }
        ]

        self.GroupStorage = [
            {
                'self': 'rest/group/grupo1',
                'name': 'grupo1'
            },
            {
                'self': 'rest/group/grupo2',
                'name': 'grupo2'
            }
        ]

    def get_users(self):
        #return make_response(jsonify({'error': 'Not found'}), 201)
        return jsonify(self.storage)

    def get_userById(self, id):
        d = [user for user in self.storage if user['id'] == id]
        if len(d) == 0:
            abort(404)
        return jsonify(d)

    def get_UserDataByID(self, id, data):
        d = [user for user in self.storage if user['id'] == id]
        if len(d) == 0:
            abort(404)
        return jsonify({"self": d[0]['self']+"/"+str(data), str(data): d[0][data]})

    def updatae_userDataById(self, id, data, json_object):
        d = [user for user in self.storage if user['id'] == id]
        if len(d) == 0:
            abort(404)
        d[0][data] = json_object.get(data, d[0][data])
        return jsonify(d)

    def delete_userDatabyID(self, id, data):
        d = [user for user in self.storage if user['id'] == id]
        print type(d)
        if len(d) == 0:
            abort(404)
        del d[0][data]
        return make_response(jsonify({'Succes': 'Element Deleted'}), 201)

    def add_user(self, json_object):
        id = self.storage[-1]['id'] + 1
        d = [user for user in self.storage if user['alias'] == json_object['alias']]
        if len(d) != 0:
            abort(400)
        new_user = {
            'self': "rest/user/" + str(id),
            'id': id,
            'alias': json_object['alias'],
            'name': json_object['name'],
            'surname': json_object['surname'],
            'age': json_object.get('age', "")
        }
        self.storage.append(new_user)

        return make_response(jsonify(new_user), 201)

    def delete_user(self, id):
        d = [user for user in self.storage if user['id'] == id]
        if len(d) == 0:
            abort(404)
        self.storage.remove(d[0])
        return make_response(jsonify({'Succes': 'Element Deleted'}), 201)

    def get_group(self):
        return jsonify(self.GroupStorage)

    def create_Group(self, json_object):
        d = [user for user in self.storage if user['name'] == json_object['name']]
        if len(d) != 0:
            abort(400)
        new_grupo = {
            'self': 'rest/group/' + str(json_object['name']),
            'name': json_object['name']
        }
        self.GroupStorage.append(new_grupo)
        return make_response(jsonify(new_grupo), 201)