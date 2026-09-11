"""Tests for Homework 1, Problem 5."""

import unittest

from p5_Evra_David import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    def test_capitalization(self):
        self.assertEqual(caesar_cipher("AbCd", 2), "CdEf")

    def test_spaces_and_punctuation(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_wraparound(self):
        self.assertEqual(caesar_cipher("Xyz", 3), "Abc")

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("Abc", -1), "Zab")

    def test_large_shift(self):
        self.assertEqual(caesar_cipher("XYZ", 29), "ABC")

    def test_empty_text(self):
        self.assertEqual(caesar_cipher("", 10), "")

    def test_decryption(self):
        self.assertEqual(caesar_decipher("Khoor, Zruog!", 3), "Hello, World!")

    def test_round_trip(self):
        message = "Caesar Cipher 101!"
        encrypted = caesar_cipher(message, -55)
        self.assertEqual(caesar_decipher(encrypted, -55), message)


class TestLetterFrequency(unittest.TestCase):
    def test_frequency_ignores_case_and_nonletters(self):
        frequencies = letter_frequency("Aa Bb! zZ 123 e")

        self.assertEqual(frequencies["a"], 2)
        self.assertEqual(frequencies["b"], 2)
        self.assertEqual(frequencies["e"], 1)
        self.assertEqual(frequencies["z"], 2)
        self.assertEqual(frequencies["c"], 0)
        self.assertEqual(len(frequencies), 26)

    def test_empty_frequency(self):
        frequencies = letter_frequency("")

        self.assertEqual(len(frequencies), 26)
        for count in frequencies.values():
            self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
