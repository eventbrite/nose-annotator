try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import (
    find_packages,
    setup,
)

name = 'nose-annotator'
setup(
    name=name,
    version='1.0.1',
    description='Plugin to annotate testcases and produce a mapping .csv file of [testcase name],[annotation]',
    author='Kip Gebhardt',
    author_email='kip@eventbrite.com',
    url='http://github.com/eventbrite/%s' % name,
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'nose.plugins.0.10': [
            'nose_annotator = nose_annotator.plugin:NoseAnnotator',
        ]
    },
)
