## nose-annotator

## Summary
A generic annotation decorator for Python tests run under `nosetests` that outputs namespaced mappings to `.csv` files

## Usage
Annotate a test case with a TestRail test case id:
```
import unittest
from nose_annotator.plugin import nose_annotator

class TestSampleClass(unittest.TestCase):

    @nose_annotator('testrail', '2729')
    def test_numbers(self):
        assert 1 == 1
```

## Quick Start
See `examples/test_sample.py` file for annotation examples.

Follow the instructions below to see plugin in action.
```
$ git clone https://github.com/eventbrite/nose-annotator.git
$ cd nose-annotator
$ sudo pip install nose
$ sudo easy_install .
$ nosetests examples --with-nose-annotator
$ tail -n +1 *.csv
==> EmoticonAnnotationFile_mapping.csv <==
TestSampleClass:test_numbers,:)

==> NumericAnnotationFile_mapping.csv <==
TestSampleClass:test_numbers,123
TestSampleClass2:test_numbers,321

==> StringAnnotationFile_mapping.csv <==
TestSampleClass:test_strings,This is an annotation
TestSampleClass2:test_strings,This is an annotation
```
