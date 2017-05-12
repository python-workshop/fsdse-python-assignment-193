from unittest import TestCase


class TestBuild(TestCase):
    #check_if_a&b_are_empty
    #check_if_it_add_or_sum_it

    def test_check_if_a_and_b_are_empty(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

        result11 = build(None, None)
        self.assertEqual(False,result11)

    def test_check_if_it_add_or_sum_it(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

        result11 = build(3, 2)
        self.assertTrue(5, result11)


