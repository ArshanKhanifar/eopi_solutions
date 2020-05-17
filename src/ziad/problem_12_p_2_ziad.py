from protocol.problem_12_p_2 import Problem12P2
import collections


class Problem12P2Ziad(Problem12P2):
  def is_anonymous_letter_constructable(self, anonymous_letter, text_for_magazine):
    # return self.is_letter_constructible_from_magazine(anonymous_letter, text_for_magazine)
    # return self.is_letter_constructible_from_magazine_2(anonymous_letter, text_for_magazine)
    return self.is_letter_constructible_from_magazine_3(anonymous_letter, text_for_magazine)

  # Method 1
  def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_hash_table = self.__build_hash_table_for(letter_text)
    magazine_hash_table = self.__build_hash_table_for(magazine_text)

    for character in letter_hash_table:
      if not letter_hash_table[character] <= magazine_hash_table[character]:
        return False

    return True

  def __build_hash_table_for(text):
    new_hash_table = {}

    for char in text:
      if char not in new_hash_table:
        new_hash_table[char] = 1
      else:
        new_hash_table[char] += 1

    return new_hash_table

  # Method 2
  # Using Python's built-in Collections.counter
  def is_letter_constructible_from_magazine_2(letter_text, magazine_text):
    char_frequency_for_letter_text = Collections.Counter(letter_text)

    for char in magazine_text:
      if char in char_frequency_for_letter_text:
        char_frequency_for_letter_text -= 1
        if char_frequency_for_letter_text[char] == 0:
          del char_frequency_for_letter_text[char]
          if not char_frequency_for_letter_text:
            return True
  
    return not char_frequency_for_letter_text

  # Method 3
  # Insane one-liner....
  # but what happens in this case? {a:1, b:2} - {c:1, d:2}?
  def is_letter_constructible_from_magazine_3(letter_text, magazine_text):
    return (not Collections.Counter(letter_text) - Collections.Counter(magazine_text))
