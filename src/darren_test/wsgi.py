from flask import Flask, request, Response, json ,jsonify,abort


application = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'Darren',
        'physics': 80,
        'maths': 60,
        'chemistry': 45
    },
    {
        'id': 2,
        'name': 'Jerry',
        'physics': 50, 
        'maths': 45,
        'chemistry': 45
    }
]

class JsonResponse(Response):
	def __init__(self, json_dict, status=200):
		super().__init__(response=json.dumps(json_dict), status=status, mimetype="application/json")

@application.route('/', methods=['GET'])
def student():
   return jsonify({'students':students})

@application.route('/get/<int:indexId>',methods=["GET"])
def get_id(indexId):
   studentId = [student for student in students if student['id'] == indexId]
   if len(studentId) == 0:
      abort(404)
   return jsonify({'students':studentId[0]})

@application.route('/add', methods=['POST'])
def add():
	if not request.json or not 'name' in request.json:    
		abort(400)

	student = {
		'id': students[-1]['id'] + 1,
		'name': request.json['name'],
		'physics': request.json.get('physics',""),
		'maths': request.json.get('maths',""),
		'chemistry': request.json.get('chemistry',"")
		}
	
	students.append(student)
	return jsonify({'students':student}), 201

@application.route('/delete/<int:indexId>', methods=['DELETE'])
def delete_method(indexId):
	if request.method == 'DELETE':
		studentId = [student for student in students if student['id'] == indexId]
		if len(studentId) == 0:
			abort(404)
		students.remove(studentId[0])
		return jsonify({'student removed': True})

@application.route('/update', methods=['PUT'])
def update_results(indexId):
	if request.method == 'PUT':
		studentId = [student for student in students if student['id'] == indexId]
	if len(studentId) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) != str:
		abort(400)
	if 'physics' in request.json and type(request.json['physics']) != int:
		abort(400)
	if 'maths' in request.json and type(request.json['maths']) != int:
		abort(404)
	if 'chemistry' in request.json and type(request.json['chemistry']) != int:
		abort(400)

	studentId[0]['name'] = request.json.get('name',studentId[0]['name'])
	studentId[0]['physics'] = request.json.get('physics',studentId[0]['physics'])
	studentId[0]['maths'] = request.json.get('maths',studentId[0]['maths'])
	studentId[0]['chemistry'] = request.json.get('chemistry',studentId[0]['chemistry'])
	return jsonify({'Updated Student':studentId[0]})

if __name__ == '__main__':
	application.run()

#curl -i -H "Content-Type: application/json" -X POST -d '{\"name\":\"Sivu\",\"physics\":30,\"maths\":90,\"chemistry\":10}' http://127.0.0.1:5000/results
#curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"Sivu\"}" http://127.0.0.1:5000/results