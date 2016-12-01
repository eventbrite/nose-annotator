## nose-annotator

## Summary
A generic annotation decorator for Python tests run under `nosetests` that outputs namespaced mappings to `.csv` files

## Quick Start
See `examples/test_sample.py` file for annotation examples.
Follow the instructions below to see plugin in action
```
$ git clone https://github.com/rv-kip/nose-annotator.git
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
