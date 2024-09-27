# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

from c07_wed04_review import *
from unittest import TestCase


class TestReview(TestCase):

    # km_to_miles
    def test_km_to_miles_valid(self):
        print("test_km_to_miles_valid")
        valid = [0, 10, 5.0, 3.2]
        for v in valid:
            self.assertAlmostEqual(km_to_miles(v), v * 0.621371192, 5)

    def test_km_to_miles_negative(self):
        print("test_km_to_miles_negative")
        invalid = [-4, -10, -5.0, -7.2]
        for v in invalid:
            with self.assertRaises(ValueError):
                km_to_miles(v)

    # consecutive_char
    def test_consecutive_char_valid(self):
        print("test_consecutive_char_valid")
        self.assertTrue(consecutive_char("hello"))
        self.assertFalse(consecutive_char("world"))

    def test_consecutive_char_invalid_type(self):
        print("test_consecutive_char_invalid_type")
        invalid = [10, [10], None]
        for v in invalid:
            with self.assertRaises(TypeError):
                consecutive_char(v)

    # duplicate
    def test_duplicate_valid(self):
        print("test_duplicate_valid")
        self.assertTrue(duplicate("hello"))
        self.assertFalse(duplicate("world"))
    
    def test_duplicate_invalid_type(self):
        print("test_duplicate_invalid_type")
        invalid = [10, [10], None]
        for v in invalid:
            with self.assertRaises(TypeError):
                duplicate(v)
    
    # max_value
    def test_max_value_valid(self):
        print("test_max_value_valid")
        self.assertEqual(max_value(10, 20, 30), 30)

    def test_max_value_invalid_type(self):
        print("test_max_value_invalid_type")
        with self.assertRaises(TypeError):
            max_value("10", "20", "30")

if __name__ == '__main__':  
    import unittest
    unittest.main()