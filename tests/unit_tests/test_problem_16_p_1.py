import pytest
from vlad.problem_16_p_1_vlad import Problem16P1Vlad


class TestProblem16P1(object):
    def instantiate_solution(self):
        return Problem16P1Vlad()

    """
    the return score_combinations is a list of lists where each list is a 
    possible combination. The index i of the inner list signifies the number 
    play_scores[i] you need
    """
    @pytest.mark.parametrize("final_score, play_scores, num_combinations", [
        (2, [2, 3, 7], 1),  #{(1, 0, 0)}
        (3, [2, 3, 7], 1),  #{(0, 1, 0)}
        (4, [2, 3, 7], 1),  #{(2, 0, 0)}
        (5, [2, 3, 7], 1),  #{(1, 1, 0)}
        (6, [2, 3, 7], 2),  #{(3, 0, 0), (0, 2, 0)}
        (7, [2, 3, 7], 2),  #{(2, 1, 0), (0, 0, 1)}
        (8, [2, 3, 7], 2),  #{(4, 0, 0), (1, 2, 0)}
        (9, [2, 3, 7], 3),  #{(1, 0, 1), (0, 3, 0), (3, 1, 0)}
        (10, [2, 3, 7], 3),  #{(0, 1, 1), (2, 2, 0), (5, 0, 0)}
        (11, [2, 3, 7], 3),  #{(2, 0, 1), (1, 3, 0), (4, 1, 0)}
        (12, [2, 3, 7], 4),  #{(1, 1, 1), (0, 4, 0), (3, 2, 0), (6, 0, 0)}
    ])
    def test_number_of_score_combinations(
            self, final_score, play_scores, num_combinations):
        assert self.instantiate_solution().number_of_score_combinations(
            final_score, play_scores) == num_combinations
