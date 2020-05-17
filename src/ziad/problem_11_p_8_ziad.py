from protocol.problem_11_p_8 import Problem11P8
import heapq


class Problem11P8Ziad(Problem11P8):
    def kth_largest_element(self, non_sorted_list, k):
    	# return self.find_kth_largest_naive(k, non_sorted_list)
    	# return self.find_kth_largest_heap(k, non_sorted_list)
    	return self.find_kth_largest_quick_select(k, non_sorted_list, 0, len(non_sorted_list) - 1)

	# Method 1
	# trivial solution: sort array and return the kth element
	# time: O(nlogn)
	def find_kth_largest_naive(k, arr):
  		arr.sort(reverse=True)
  		return arr[k-1]

	# Method 2
	# use min heap.. similar to last week's stuff

	# Method 3
	# solution using the Quick Select algorithm
	# time: average case O(n), worst case O(n^2)
	def find_kth_largest_quick_select(k, arr, floor, ceiling):
  		position = partition(arr, floor, ceiling)

  		# If position is same as k 
  		if (position - floor == k - 1): return arr[position] 
  		elif (position - floor > k - 1):
    		return find_kth_largest_quick_select(k, arr, floor, position - 1)
  		else: 
    		return find_kth_largest_quick_select(k - position + floor - 1, arr, position + 1, ceiling)

	def partition(arr, floor, ceiling):
  		pivot = arr[ceiling]

  		for i in range(floor, ceiling):
    		if arr[i] > pivot:
      			swap(arr, i, floor)
      			floor += 1

  		swap(arr, ceiling, floor)
  		return floor

  	def swap(arr, left, right):
  		arr[left], arr[right] = arr[right], arr[left]
