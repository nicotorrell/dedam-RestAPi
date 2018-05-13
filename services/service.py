

class Server:

    def __init__(self, database):
        self.db = database

    def get_users(self):
        users = self.db.get_users()
        return users

    def get_userByid(self, id):
        user = self.db.get_userById(id)
        return user

    def get_UserDataByID(self, id ,data):
        datos = self.db.get_UserDataByID(id, data)
        return datos

    def updatae_userDataById(self, id, data, json_object):
        response = self.db.updatae_userDataById(id, data, json_object)
        return response

    def delete_userDatabyID(self, id, data):
        response = self.db.delete_userDatabyID(id, data)
        return response

    def add_user(self, json_object):
        added_user = self.db.add_user(json_object)
        return added_user

    def delete_user(self, id):
        deleted_user = self.db.delete_user(id)
        return deleted_user

    def get_group(self):
        groups = self.db.get_group()
        return groups

    def create_Group(self, json_object):
        grupos = self.db.create_Group(json_object)
        return grupos