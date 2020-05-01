
# word
# one of each
# one fish two fish red fish blue fish
# one,two,three
# one,\ntwo,\nthree
# car: carpet as java: javascript!!&@$%^&
# testing, 1, 2 testing
# go Go GO Stop stop
# First: don't laugh. Then: don't cry.
# Joe can't tell between 'large' and large.
# Joe can't tell between app, apple and a.
#  multiple   whitespaces
#  ,\n,one,\n ,two \n 'three'
#  hey,my_spacebar_is_broken
#  ''hey''
#  rah rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance
 
# import unittest

# class WordCountTest(unittest.TestCase):
#     def test_alternating_word_separators_not_detected_as_a_word(self):
#         self.assertEqual(
#             count_words(",\n,one,\n ,two \n 'three'"), {"one": 1, "two": 1, "three": 1}
#         )
#     def test_with_quotations(self):
#         self.assertEqual(
#             count_words("Joe can't tell between 'large' and large."),
#             {"joe": 1, "can't": 1, "tell": 1, "between": 1, "large": 2, "and": 1},
#         )

#     def test_non_alphanumeric(self):
#         self.assertEqual(
#             count_words("hey,my_spacebar_is_broken"),
#             {"hey": 1, "my": 1, "spacebar": 1, "is": 1, "broken": 1},
#         )
#     def test_multiple_apostrophes_ignored(self):
#         self.assertEqual(count_words("''hey''"), {"hey": 1})
		
#     def test_multiple_occurrences_of_a_word(self):
#         self.assertEqual(
#             count_words("one fish two fish red fish blue fish"),
#             {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1},
#         )
#     def test_with_apostrophes(self):
#         self.assertEqual(
#             count_words("First: don't laugh. Then: don't cry."),
#             {"first": 1, "don't": 2, "laugh": 1, "then": 1, "cry": 1},
#         )
#     def test_ignore_punctuation(self):
#         self.assertEqual(
#             count_words("car: carpet as java: javascript!!&@$%^&"),
#             {"car": 1, "carpet": 1, "as": 1, "java": 1, "javascript": 1},
#         )

# if __name__ == "__main__":
#     unittest.main()


# %%
