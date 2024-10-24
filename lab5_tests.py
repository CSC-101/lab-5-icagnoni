import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_1(self):
        first_time = data.Time(2, 10, 15)
        second_time = data.Time(2, 20, 50)
        result = lab5.time_add(first_time, second_time)
        self.assertEqual(result, data.Time(4, 31, 5))

    def test_time_2(self):
        time1 = data.Time(2, 59, 20)
        time2 = data.Time(0, 0, 45)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result, data.Time(3, 0, 5))

    # Part 4
    def test_descending_1(self):
        self.assertTrue(lab5.is_descending([10, 8, 6, 4, 2]))

    def test_is_descending_2(self):
        self.assertFalse(lab5.is_descending([10, 8, 6, 2, 4]))

    # Part 5
    def test_largest_between_1(self):
        lst = [15, 20, 8, 20, 35, 30, 10]
        result = lab5.largest_between(lst, 2, 5)
        self.assertEqual(result, 4)

    def test_largest_between_2(self):
        lst = [5, 10, 20, 25, 30]
        result = lab5.largest_between(lst, 4, 2)
        self.assertIsNone(result)

    # Part 6

    def test_furthest_from_origin_normal_case(self):
        points = [data.Point(1, 0), data.Point(2, 1), data.Point(3, 3)]
        result = lab5.furthest_from_origin(points)
        self.assertEqual(result, 2)

    def test_furthest_from_origin_empty_list(self):
        points = []
        result = lab5.furthest_from_origin(points)
        self.assertIsNone(result)




if __name__ == '__main__':
    unittest.main()
