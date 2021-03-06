import pytest
from vlad.problem_5_p_18_var1_vlad import Problem5P18Var1Vlad


class TestProblem5P18Var1(object):
    def instantiate_solution(self):
        return Problem5P18Var1Vlad()

    @pytest.mark.parametrize("dimension, spiral_ordered_matrix", [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
        (5, [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
    ])
    def test_make_spiral_ordered_matrix(self, dimension, spiral_ordered_matrix):
        assert self.instantiate_solution().make_spiral_ordered_matrix(dimension) == spiral_ordered_matrix
