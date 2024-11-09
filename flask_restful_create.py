# -*- coding: utf-8 -*-
"""
文件描述：
    id = 2
    使用python第三方模块flask-restful快速完成Restful风格的API开发
"""
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

persons = [{'name': 'Alex', 'city': 'New York'},{'name': 'Bob', 'city': 'London'}]

def abort_person_doesnt_exist(_id):
    if _id not in range(len(persons)):
        abort(404, message=f"id {_id} doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, default='')
parser.add_argument('city', type=str, default='')


class Person(Resource):
    def get(self, _id):
        abort_person_doesnt_exist(_id)
        return persons[_id]

    def delete(self, _id):
        abort_person_doesnt_exist(_id)
        person = persons[_id]
        persons.remove(person)
        return person

    def put(self, _id):
        abort_person_doesnt_exist(_id)
        args = parser.parse_args()
        if args['city']:
            persons[_id]["city"] = args['city']
        if args['name']:
            persons[_id]["name"] = args['name']
        return persons[_id]


class Persons(Resource):
    def get(self):
        return persons

    def post(self):
        args = parser.parse_args()
        persons.append({'name': args['name'], 'city': args['city']})
        return args


api.add_resource(Persons, '/persons')
api.add_resource(Person, '/persons/<int:_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)