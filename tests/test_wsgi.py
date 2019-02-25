import json
import pytest
from darren_test.wsgi import *

@pytest.fixture
def client(request):
	test_client = application.test_client()

	def teardown():
		pass # databases and resourses have to be freed at the end. But so far we don't have anything

	request.addfinalizer(teardown)
	return test_client

def json_of_response(response):
	"""Decode json from response"""
	return json.loads(response.data.decode('utf8'))

@pytest.mark.parametrize('idNum, name, phyScore ,mathScore, chemScore',
                           [
                               (1,'Darren',80,60,45),
                               (2, 'Jerry',50,45,45),
                           ]
                        )
def test_get(idNum, name, phyScore ,mathScore, chemScore):
	with application.test_client() as test_client:
		response = test_client.get("/get/{}".format(idNum))
		assert response.status_code == 200
		studentId = [student for student in students if student['id'] == idNum]
		assert studentId[0] == {'id': idNum,'name': name,'physics': phyScore,'maths': mathScore,'chemistry': chemScore}

@pytest.mark.parametrize('idNum, name, phyScore ,mathScore, chemScore',
                           [
                               (3,'Darren',80,60,45),
                               (4,'Harry',10,10,10),
                               (5,'George',40,30,50),
                               (6,'Potter',40,30,50),
                               (7,'Ron',40,30,50)
                           ]
                        )
def test_add(idNum, name, phyScore ,mathScore, chemScore):
	with application.test_client() as test_client:
		response = test_client.post('/add',data=json.dumps({'name':name,'physics':phyScore,'maths':mathScore,'chemistry':chemScore}),content_type='application/json',)
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 201
		assert json_of_response(response) == {'students' : {'id': idNum, 'name' : name , 'physics' : phyScore , 'maths' : mathScore, 'chemistry': chemScore }}

