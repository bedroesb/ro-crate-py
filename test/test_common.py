import os
import sys
import shutil
import tempfile
import unittest



class BaseTest(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="rocrate_test_")

        #copy test data
        shutil.copytree(os.path.abspath(os.path.join('test', 'test-data')), os.path.join(self.tmpdir, 'test-data'))
        self.test_wf_dir = os.path.join(self.tmpdir, 'test-data', 'test-wf')
        self.assertTrue(os.path.isdir(self.test_wf_dir))
