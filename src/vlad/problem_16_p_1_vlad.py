from protocol.problem_16_p_1 import Problem16P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem16P1Vlad(Problem16P1):
    def number_of_score_combinations(self, final_score, play_scores):
        # return len(self.try_it_all(final_score, play_scores))
        # return len(self.some_recursive_shit(final_score, play_scores))
        # return len(self.some_recursive_shit_with_good_memeory(final_score,
        #                                                    play_scores))
        return self.dp_af(final_score, play_scores)

    """"
    if we call x = final_score // min(play_scores) 
    then runtime is O(max(play_scores) ** x) space is O(len(play_scores))
    Terrible run time!
    """
    def try_it_all(self, final_score, play_scores):
        score_combinations = set()

        # first find min val from all play scores
        min_play_score = min(play_scores)

        # now get the amount or more than needed of the min score to make final
        min_play_score_needed = final_score // min_play_score

        # this is how much of each score to use at any point
        play_score_count = [0] * len(play_scores)
        play_score_count_hlpr = [0] * len(play_scores)
        while play_score_count[len(play_scores) - 1] < min_play_score_needed:
            play_score_count_hlpr[0] += 1
            score_sum = 0   # this is the sum of all scores using the count
            for i in range(len(play_score_count)):
                if i:   # exclude first element since there is none before it
                    play_score_count_hlpr[i] = play_score_count_hlpr[i-1] // \
                                               (min_play_score_needed + 1)
                play_score_count[i] = play_score_count_hlpr[i] % \
                                      (min_play_score_needed + 1)
                score_sum += play_score_count[i] * play_scores[i]
            if score_sum == final_score:
                score_combinations.add(tuple(play_score_count))
        return score_combinations

    """
    it goes through every possible combination so it's literally the same as 
    above iterative one except it uses a shit tone of memory making new lists 
    """
    def some_recursive_shit(self, final_score, play_scores):
        def inner_func(goal_score, play_score_count):
            if goal_score < 1:
                return
            for i, score in enumerate(play_scores):
                if goal_score == score:
                    play_score_count_copy = list(play_score_count)
                    play_score_count_copy[i] += 1
                    score_combinations.add(tuple(play_score_count_copy))
            for i, score in enumerate(play_scores):
                play_score_count_copy = list(play_score_count)
                play_score_count_copy[i] += 1
                inner_func(goal_score - score, list(play_score_count_copy))

        score_combinations = set()
        play_score_count = [0] * len(play_scores)
        inner_func(final_score, play_score_count)
        return score_combinations

    def some_recursive_shit_with_good_memeory(self, final_score, play_scores):
        def inner_func(goal_score, play_score_count):
            if goal_score < 1:
                return
            for i, score in enumerate(play_scores):
                if goal_score == score:
                    play_score_count[i] += 1
                    score_combinations.add(tuple(play_score_count))
                    play_score_count[i] -= 1
            for i, score in enumerate(play_scores):
                play_score_count[i] += 1
                inner_func(goal_score - score, play_score_count)
                play_score_count[i] -= 1

        score_combinations = set()
        play_score_count = [0] * len(play_scores)
        inner_func(final_score, play_score_count)
        return score_combinations

    def dp_af(self, final_score, play_score):
        combo_count_cache = [[1] + [0] * (final_score) for _ in play_score]

        for i in range(len(play_score)):
            for j in range(1, final_score + 1):
                without_score = (combo_count_cache[i-1][j] if i > 0 else 0)
                with_score = (combo_count_cache[i][j - play_score[i]]
                              if j >= play_score[i] else 0)
                combo_count_cache[i][j] = (with_score + without_score)
        return combo_count_cache[-1][-1]
