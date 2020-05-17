from protocol.problem_11_p_8_var1 import Problem11P8Var1
import random


class Problem11P8Var1Ziad(Problem11P8Var1):
    def find_median(self, non_sorted_list):
    	return self.find_median_with_quick_select(non_sorted_list)

    # Method 1
    # I ended up taking a hint from a really clean solution developed by by Russell Cohen
    # Credit: https://rcoh.me/posts/linear-time-median-finding/
    def find_median_with_quick_select(non_sorted_list, pivot_fn=random.choice)
    # list is of odd-length
    if len(non_sorted_list) % 2 == 1:
    	return quick_select(non_sorted_list, len(non_sorted_list), pivot_fn)

    # list is of even length, in which case we want to find the number in between the left and right "pseudo-medians"
    return 0.5 * (quick_select(non_sorted_list, len(non_sorted_list) / 2 - 1, pivot_fn) + 
    	quick_select(non_sorted_list, len(non_sorted_list) / 2, pivot_fn))

    def quick_select(non_sorted_list, k, pivot_fn):
    	if len(non_sorted_list) == 1:
    		return non_sorted_list[0]

    	pivot = pivot_fn(non_sorted_list)

    	lows = [item for item in non_sorted_list if item < pivot]
    	highs = [item for item in non_sorted_list if item > pivot]
    	pivots = [item for item in non_sorted_list if item == pivot]

    	# there are k or more elements in the list of lows, indicating that the median is in this list
    	if k < len(lows): 
    		return quick_select(lows, k, pivot_fn)
    	elif k > len(lows) + len(pivots):
    		return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)
    	else:
    		# lucky us, we have landed on the median!
    		return pivots[0]

    # NOTE: we can improve this algorithm objectively better by modifying the way in which we choose the pivot
    # instead of choosing it randomly. This method is known as the "median of medians"
    		

