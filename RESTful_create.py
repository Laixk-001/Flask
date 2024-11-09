# -*- coding: utf-8 -*- 
from flask import Flask, request, jsonify

app = Flask(__name__)

persons = [{'name': 'Alex', 'city': 'New York'},{'name': 'Bob', 'city': 'London'}]

@app.route('/persons',methods=['GET'])
def index():
    return jsonify(persons)

@app.route('/persons/<int:_id>',methods=['GET'])
def get_person_by_id(_id):
    if _id in range(len(persons)):
        return jsonify(persons[_id])
    else:
        return jsonify(f"{_id} is not in db.")

@app.route('/persons/<int:_id>', methods=['PUT'])
def update_person_by_id(_id):
    data = request.json
    if data['city']:
        persons[_id]["city"] = data['city']
    if data['name']:
        persons[_id]["name"] = data['name']
    return jsonify({"person": data})


@app.route('/persons/<int:_id>', methods=['DELETE'])
def delete_person_by_id(_id):
    if _id in range(len(persons)):
        person = persons[_id]
        persons.remove(person)
        return jsonify(person)
    else:
        return jsonify(f"{_id} is not in db.")

@app.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    persons.append(data)
    return jsonify({"person": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)