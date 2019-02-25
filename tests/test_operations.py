import sys
import pytest
from darren_test.operations import Ops

operations = Ops()

@pytest.mark.addoperation
def test_addition(answer = 5,x = 3,y = 2):
	assert answer == operations.get_addition(x,y)
	print("Test Addition Passed")

@pytest.mark.suboperation
def test_subtraction(answer = 0,x = 1,y = 1):
	assert answer == operations.get_subtraction(x,y)
	print("Test Subtraction Passed")

@pytest.mark.muloperation
def test_multiplication(answer = 20,x = 10,y = 2):
	assert answer == operations.get_multiplication(x,y)
	print("Test Multiplication Passed")

@pytest.mark.divoperation
def test_division(answer = 2,x = 12,y = 6):
	assert answer == operations.get_division(x,y)
	print("Test Division Passed")

test_addition(5,3,2)			#passed
test_subtraction(0,1,1)			#passed
test_multiplication(20,10,2)	#failed
test_division(2,12,6)			#failed

# test_addition(3,2)			#passed
# test_subtraction(1,1)			#passed
# test_multiplication(10,2)		#failed
# test_division(12,6)			#failed