from protocol.problem_12_p_2 import Problem12P2


class Problem12P2Arshan(Problem12P2):
    def is_anonymous_letter_constructable(self, anonymous_letter, text_for_magazine):
        return self.more_optimized(anonymous_letter, text_for_magazine)
        return self.brute_force(anonymous_letter, text_for_magazine)

    def more_optimized(self, anonymous_letter, text_for_magazine):
        anonymous_lookup = self._count_num_chars(anonymous_letter)
        for c in text_for_magazine:
            if c in anonymous_lookup:
                anonymous_lookup[c] -= 1
                if anonymous_lookup[c] == 0:
                    del anonymous_lookup[c]
                    if not anonymous_lookup:
                        return True
        return not anonymous_lookup

    def _count_num_chars(self, word):
        lookup = {}
        for char in word:
            if char not in lookup:
                lookup[char] = 0
            lookup[char] += 1
        return lookup

    def brute_force(self, anonymous_letter, text_for_magazine):
        lookup_anonymous, lookup_magazine = [self._count_num_chars(letter) for letter in [
            anonymous_letter, text_for_magazine
        ]]
        for c in lookup_anonymous:
            if c not in lookup_magazine:
                return False
            if lookup_magazine[c] < lookup_anonymous[c]:
                return False
        return True

