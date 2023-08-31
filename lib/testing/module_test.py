from lib.absolute_package.package1 import module1
from lib.absolute_package.package1.module1 import function1
from lib.absolute_package.package2.subpackage1.module6 import function1


class TestModule:
    '''placeholder test'''

    def test_module(self):
        assert(1==1)