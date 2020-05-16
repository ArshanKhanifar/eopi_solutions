from arshan.problem_11_p_8_arshan import Problem11P8Arshan
from protocol.problem_11_p_8_var2 import Problem11P8Var2


class Problem11P8Var2Arshan(Problem11P8Var2):
    def kth_largest_element_with_dups(self, non_sorted_list, k):
        return Problem11P8Arshan().books_solution_cool_one_pass(
            non_sorted_list,
            k
        )
