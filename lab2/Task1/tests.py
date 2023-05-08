import unittest

from main import (
    average_word_length,
    average_sentence_length,
    top_n_grams,
    count_sentences,
    count_non_declarative
)


class TestAverageWordLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(average_word_length(""), 0)

    def test_normal(self):
        self.assertEqual("Hello World!", 5)


class TestAverageSentenceLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(average_sentence_length("      !!!!"), 0)

    def test_normal(self):
        self.assertEqual("Hello World! You are beautiful!", 2.5)


class TestCountSentences(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(count_sentences(" ! ! ! ! 4"), 0)

    def test_normal(self):
        self.assertEqual(count_sentences("Hello World! You are beautiful!"), 2)


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(count_non_declarative("I don't like python,really."), 0)

    def test_normal(self):
        self.assertEqual(count_non_declarative("I don't like python,really!"), 1)


class TestNGrams(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(top_n_grams(""), [])

    def test_normal(self):
        self.assertEqual(top_n_grams('Those are words.'), ['Those are words'])
