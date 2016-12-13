import io
import os

from nose.plugins import Plugin

KEY = 'nose_annotator'
TESTRAIL = 'testrail'

def nose_annotator(key=None, value=None):
    """Decorator
    Ex @nose_annotator('foo', 123) will output to foo.csv with
    TESTCLASS:TESTCASE, 123
    """
    def wrap_ob(ob):
        if not getattr(ob, KEY, None):
            setattr(ob, KEY, [])
        getattr(ob, KEY, []).append({key: value})
        return ob
    return wrap_ob


class NoseAnnotator(Plugin):
    name = 'nose-annotator'

    def options(self, parser, env=os.environ):
        super(NoseAnnotator, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoseAnnotator, self).configure(options, conf)
        if not self.enabled:
            return

    def startTest(self, test):
        """Collect any annotations for this testcase"""
        self.test_class, self.test_name = self.get_test_class_name(test)
        self.annotations = self.get_test_annotations(test)
        self.result = {}

    def stopTest(self, test):
        """Atomically write out annotations to appropriate mapping file"""
        if self.annotations and len(self.annotations):
            test_class, test_name = self.get_test_class_name(test)
            for annotation in self.annotations:
                for key, value in annotation.iteritems():
                    mapping_file = self.get_test_mapping_file_name(key)
                    with io.open(mapping_file, 'ab') as f:
                        f.write('%s:%s,%s' % (test_class, test_name, value) + "\n")

    def get_test_annotations(self, test):
        test_method = getattr(test.test, self.test_name, None)
        annotations = getattr(test_method, KEY, None)
        return annotations

    def get_test_class_name(self, test):
        test_class = test.id().split('.')[-2]
        test_name = test.id().split('.')[-1]
        return test_class, test_name

    def get_test_mapping_file_name(self, key_name):
        filename = key_name + '_mapping.csv'
        if os.environ.get(key_name.upper(), None):
            filename = os.environ.get(key_name.upper())

        return filename
