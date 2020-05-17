import random
from protocol.problem_11_p_8 import Problem11P8


class Problem11P8Arshan(Problem11P8):
    def kth_largest_element(self, non_sorted_list, k):
        return self.books_solution_cool_one_pass(non_sorted_list, k)
        return self.my_solution_from_books_idea(non_sorted_list, k)
        return self.keep_highest_n(non_sorted_list, k)
        return self.naive_solution(non_sorted_list, k)

    def naive_solution(self, non_sorted_list, k):
        return sorted(non_sorted_list, reverse=True)[k-1]

    def repartition_around_pivot_idx(self, A, left, right, pivot_idx):
        pivot = A[pivot_idx]
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        new_pivot_idx = left
        for j in range(len(A)):
            if A[j] > pivot:
                A[new_pivot_idx], A[j] = A[j], A[new_pivot_idx]
                new_pivot_idx += 1
        A[new_pivot_idx], A[right] = A[right], A[new_pivot_idx]
        return new_pivot_idx

    """
    In the book they do it by one-pass
    """
    def books_solution_cool_one_pass(self, non_sorted_list, k):
        A = non_sorted_list
        pivot_idx = random.randrange(len(A))
        new_pivot_idx = self.repartition_around_pivot_idx(A, 0, len(A) - 1, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        if new_pivot_idx < k - 1:
            return self.my_solution_from_books_idea(A[new_pivot_idx + 1:], k - new_pivot_idx - 1)
        return self.my_solution_from_books_idea(A[:new_pivot_idx], k)

    def my_solution_from_books_idea(self, non_sorted_list, k):
        pivot = random.choice(non_sorted_list)
        i = 0
        A = non_sorted_list
        for j in range(len(A)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        i = len(A) - 1
        for j in reversed(range(len(A))):
            if A[j] > pivot:
                i = j + 1
                break
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i -= 1
        # i will be pointing to the pivot value, to the left are the bigger elements.
        if i == k - 1:
            return pivot
        if i < k - 1:
            return self.my_solution_from_books_idea(A[i + 1:], k - i - 1)
        if i > k - 1:
            return self.my_solution_from_books_idea(A[:i], k)

    """
    O(nk) if k is small then this is almost linear.
          if k is a fraction of n then this becomes O(n^2).
    """
    def keep_highest_n(self, non_sorted_list, k):
        max_stack = []

        def _insert_into_sorted_stack(max_stack, key):
            inserted = False
            for i, v in enumerate(max_stack):
                if key > v:
                    max_stack.insert(i, key)
                    inserted = True
                    break
            if not inserted:
                max_stack.append(key)

        def _insert_into_stack(key, k):
            if len(max_stack) < k:
                _insert_into_sorted_stack(max_stack, key)
                return
            if key < max_stack[-1]:
                return
            max_stack.pop()
            _insert_into_sorted_stack(max_stack, key)

        for key in non_sorted_list:
            _insert_into_stack(key, k)
        return max_stack[-1]
