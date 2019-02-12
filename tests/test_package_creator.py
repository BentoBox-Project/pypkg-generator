import os

import pytest
from testfixtures import TempDirectory

from package_scaffold import package_creator


@pytest.fixture()
def dir():
    with TempDirectory() as dir:
        yield dir


def test_create_new_package(dir):
    pkg_name = 'pkg_name'
    args = {'name': pkg_name, 'path': dir.path}
    pkg_creator = package_creator.PackageCreator(args)
    pkg_creator.call()
    assert os.path.exists(os.path.join(dir.path, pkg_name))
