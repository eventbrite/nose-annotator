import unittest
from nose_annotator.plugin import nose_annotator


class TestSampleClass(unittest.TestCase):

    @nose_annotator('NumericAnnotationFile', 123)
    @nose_annotator('EmoticonAnnotationFile', ':)')
    def test_numbers(self):
        assert 1 == 1

    @nose_annotator('StringAnnotationFile', 'This is an annotation')
    def test_strings(self):
        assert 'aaa' == 'aaa'

    def test_boolean(self):
        assert True == True


class TestSampleClass2(unittest.TestCase):

    @nose_annotator('NumericAnnotationFile', 321)
    def test_numbers(self):
        assert 1 == 1

    @nose_annotator('StringAnnotationFile', 'This is an annotation')
    def test_strings(self):
        assert 'aaa' == 'aaa'

    def test_boolean(self):
        assert True == True