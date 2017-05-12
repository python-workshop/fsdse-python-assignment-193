from unittest import TestCase


class TestBuild(TestCase):

    def test_build(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")


