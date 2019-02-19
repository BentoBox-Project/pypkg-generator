import os

import pytest
from testfixtures import TempDirectory

from pypkg_generator import package_generator
from pypkg_generator import exceptions


@pytest.fixture()
def dir():
    with TempDirectory() as dir:
        yield dir


def pkg_generator(dir, pkg_name):
    args = {'name': pkg_name, 'path': dir.path}
    return package_generator.PackageGenerator(args)


def test_create_new_package(dir):
    creator = pkg_generator(dir, 'pkg_name')
    creator.call()
    assert os.path.exists(os.path.join(dir.path, creator.package_name))


def tests_no_name_error(dir):
    with pytest.raises(exceptions.ForgottenNameError) as e:
        args = {'name': '', 'path': dir.path}
        pkg_generator = package_generator.PackageGenerator(args)
        pkg_generator._is_name_empty()
    assert str(e.value) == 'The name is empty!'


def tests_dir_existst_error(dir):
    with pytest.raises(exceptions.DirectoryExistsError) as e:
        creator = pkg_generator(dir, 'pkg_name')
        creator.call()
        creator._create_dir('pkg_name')
    assert str(e.value) == 'The directory already exists'
