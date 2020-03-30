from ipynb.fs.full.assignment import *
import pytest
import numpy as np

@pytest.mark.parametrize("test_input1, test_input2, expected", [(4,10,[4,6,8,10])])
def test_eval1(test_input1, test_input2, expected):
    assert np.allclose(question_first_solution(test_input1, test_input2), expected)

@pytest.mark.parametrize("test_input1, test_input2, test_input3, test_input4, expected", [(0, 20, 9, 15, [0, 1, 2, 3, 4, 5, 6, 7, 8, -9, -10, -11, -12, -13, -14, -15, 16, 17, 18, 19])])
def test_eval2(test_input1, test_input2, test_input3, test_input4, expected):
    assert np.allclose(question_second_solution(test_input1, test_input2, test_input3, test_input4), expected)

@pytest.mark.parametrize("test_input1, test_input2, expected", [(3, 4,  [[1., 1., 1., 1.],[1., 0., 0., 1.],[1., 1., 1., 1.]])])
def test_eval3(test_input1, test_input2, expected):
    assert np.allclose(question_third_solution(test_input1, test_input2,), expected)

@pytest.mark.parametrize("test_input, expected", [([[1,2,3], [4,5,np.nan], [7,8,9], [True, False, True]], [[1., 2., 3.], [7., 8., 9.], [1., 0., 1.]])])
def test_eval4(test_input, expected):
    assert np.allclose(question_fourth_solution(test_input), expected)

@pytest.mark.parametrize("test_input1, test_input2, expected", [([97, 101, 105, 110, 109],[0,1,2,3,4],[1,2,4])])
def test_eval5(test_input1, test_input2, expected):
    assert np.allclose(question_fifth_solution(test_input1, test_input2,), expected)

@pytest.mark.parametrize("test_input, expected", [([10,10,20,10,20,20,20,30, 30,50,40,40],[3,4,2,2,1])])
def test_eval6(test_input, expected):
    assert np.allclose(question_sixth_solution(test_input), expected)

@pytest.mark.parametrize("test_input1, test_input2, expected", [([[1,2,3], [4,5,6] , [7,8,9], [10, 11, 12]], [1,2,3],[0])])
def test_eval7(test_input1, test_input2, expected):
    assert np.allclose(question_seventh_solution(test_input1, test_input2), expected)

@pytest.mark.parametrize("test_input, expected", 
[
    ([5+3j, -1-2j, 0],[-1-2j,0,5+3j]),
    ([-1j,-2j],[-2j,-1j])])
def test_eval8(test_input, expected):
    assert np.allclose(question_eighth_solution(test_input), expected)

@pytest.mark.parametrize("test_input, expected", [([1023, 5202, 6230, 1671, 1682, 5241, 4532], [0, 3, 4, 6, 1, 5, 2])])
def test_eval9(test_input, expected):
    assert np.allclose(question_ninth_solution(test_input), expected)

@pytest.mark.parametrize("expected", [([[0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0]]),
       ([[0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0]]
    )])
def test_eval10(expected):
    assert np.allclose(question_tenth_solution(), expected)