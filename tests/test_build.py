from unittest import TestCase


class TestBuild(TestCase):
    def test_sum_two(self):
        try:
            from build import sum_two
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, sum_two, None)
        self.assertEqual(sum_two(5, 7), 12)
        self.assertEqual(sum_two(-5, -7), -12)
        self.assertEqual(sum_two(5, -7), -2)