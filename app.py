from flask import Flask, request, jsonify, abort
from services.service import Server
from services.database import Database

database = Database()
server = Server(database)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)


# curl http://localhost:5000/rest/user
@app.route("/rest/user", methods=["GET"])
def get_user():
    # all_users = User.query.all()
    # result = users_schema.dump(all_users)
    return server.get_users()


# curl http://localhost:5000/rest/user/1
@app.route("/rest/user/<int:id>", methods=["GET"])
def get_UserByID(id):
    return server.get_userByid(id)


# curl http://localhost:5000/rest/user/1/alias
@app.route("/rest/user/<int:id>/<data>", methods=["GET"])
def get_UserDataByID(id, data):
    return server.get_UserDataByID(id, data)


# curl --header "Content-Type: application/json" --request PUT http://localhost:5000/rest/user/1/alias --data "{"""alias""":"""aquaman"""}"
@app.route("/rest/user/<int:id>/<data>", methods=["PUT"])
def updatae_userDataById(id, data):
    if not request.json:
        abort(400)
    json_object = request.get_json()
    return server.updatae_userDataById(id, data, json_object)


# curl http://localhost:5000/rest/user/1/alias
@app.route("/rest/user/<int:id>/<data>", methods=["DELETE"])
def delete_userDatabyID(id, data):
    return server.delete_userDatabyID(id, data)


# curl --header "Content-Type: application/json" --request POST http://localhost:5000/rest/user --data "{"""alias""":"""pikachu""","""name""":"""Eduard""","""surname""":"""martinez"""}"
# http://localhost:5000/user
@app.route("/rest/user", methods=["POST"])
def add_user():
    if not request.json or not 'alias' in request.json or not 'name' in request.json or not 'surname' in request.json:
        abort(400)
    json_object = request.get_json()
    return server.add_user(json_object)


# curl --header "Content-Type: application/json" --request DELETE http://localhost:5000/user/1
@app.route("/rest/user/<int:id>", methods=["DELETE"])
def user_delete(id):
    return server.delete_user(id)


# curl http://localhost:5000/rest/grupo
@app.route("/rest/grupo", methods=["GET"])
def get_Group():
    return server.get_group()


# curl --header "Content-Type: application/json" --request POST http://localhost:5000/rest/grupo --data "{"""name""":"""admin"""}"
@app.route("/rest/grupo", methods=["POST"])
def create_Group():
    if not request.json or not 'name' in request.json:
        abort(400)
    json_object = request.get_json()
    return server.create_Group(json_object)


if __name__ == '__main__':
    app.run(debug=True)