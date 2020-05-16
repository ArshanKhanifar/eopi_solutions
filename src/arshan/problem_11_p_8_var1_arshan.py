from arshan.problem_11_p_8_arshan import Problem11P8Arshan
from protocol.problem_11_p_8_var1 import Problem11P8Var1


class Problem11P8Var1Arshan(Problem11P8Var1):
    def find_median(self, non_sorted_list):
        prev_soln = Problem11P8Arshan()
        l = len(non_sorted_list)
        k = l >> 1
        if l & 1:
            return prev_soln.kth_largest_element(non_sorted_list, k + 1)
        else:
            return (prev_soln.kth_largest_element(non_sorted_list, k) +
                    prev_soln.kth_largest_element(non_sorted_list, k + 1))/2
