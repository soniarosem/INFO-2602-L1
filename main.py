from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

#read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  #return 'Hello World' in response


@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')  #get the parameter from url
    if pref:
        for student in data:  #iterate dataset
            if student[
                    'pref'] == pref:  #select only the students with a given meal preference
                result.append(student)  #add match student to the result
        return jsonify(result)  #return filtered set if parameter is supplied
    return jsonify(data)  #return entire dataset if no parameter supplied


#route variables
@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student[
                'id'] == id:  #filter out the students without the specified id
            return jsonify(student)


#exercise 1
@app.route('/stats')
def get_stats():
    statistics = {
        "Chicken": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Fish": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
        "Vegetable": 0,
    }

    for student in data:
        if student['programme'] in statistics:
            statistics[student['programme']] += 1

        if student['pref'] in statistics:
            statistics[student['pref']] += 1

    return jsonify(statistics)

#exercise 2
@app.route('/add/<int:a>/<int:b>')
def addition(a, b):
    return jsonify(a + b)

@app.route('/subtract/<int:a>/<int:b>')
def subtraction(a, b):
    return jsonify(a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiplication(a, b):
    return jsonify(a * b)

@app.route('/divide/<int:a>/<int:b>')
def division(a, b):
    return jsonify(a / b)

app.run(host='0.0.0.0', port=8080)
