import pytest

from arshan.problem_12_p_2_arshan import Problem12P2Arshan
from vlad.problem_12_p_2_vlad import Problem12P2Vlad


class TestProblem12P2(object):
    def instantiate_solution(self):
        return Problem12P2Arshan()
        return Problem12P2Vlad()

    @pytest.mark.parametrize("anonymous_letter, text_for_magazine, writable", [
        ('abcd', 'abcd', True),
        ('aabcd', 'abcd', False),
        ('abcd', 'aabcd', True),
        ('brother', 'volodyrotaisbher', True),
        ('hi', 'hi I am arshan', True),
        ('hii', 'hi I am arshan', False),
    ])
    def test_is_anonymous_letter_writable(self, anonymous_letter, text_for_magazine, writable):
        assert self.instantiate_solution().is_anonymous_letter_constructable(anonymous_letter, text_for_magazine) == writable
