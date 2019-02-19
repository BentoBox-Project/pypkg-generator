import os

import pytest
from testfixtures import TempDirectory

from package_scaffold import package_creator
from package_scaffold import exceptions


@pytest.fixture()
def dir():
    with TempDirectory() as dir:
        yield dir


def pkg_creator(dir, pkg_name):
    args = {'name': pkg_name, 'path': dir.path}
    return package_creator.PackageCreator(args)


def test_create_new_package(dir):
    creator = pkg_creator(dir, 'pkg_name')
    creator.call()
    assert os.path.exists(os.path.join(dir.path, creator.package_name))


def tests_no_name_error(dir):
    with pytest.raises(exceptions.ForgottenNameError) as e:
        args = {'name': '', 'path': dir.path}
        pkg_creator = package_creator.PackageCreator(args)
        pkg_creator._is_name_empty()
    assert str(e.value) == 'The name is empty!'


def tests_dir_existst_error(dir):
    with pytest.raises(exceptions.DirectoryExistsError) as e:
        creator = pkg_creator(dir, 'pkg_name')
        creator.call()
        creator._create_dir('pkg_name')
    assert str(e.value) == 'The directory already exists'
