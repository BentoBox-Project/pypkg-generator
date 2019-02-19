# -*- coding: utf-8 -*-
""" PackageCreator
This module contains the PackageCreator class
This class creates a new entire project from scratch
"""

import os

from colored import fg, attr

from .exceptions import DirectoryExistsError, ForgottenNameError
from .config import README, SETUP, LICENSE, REQUIREMENTS, PIPFILE
from .config import CODE_OF_CONDUCT, GITIGNORE, INIT_FILE, TESTS_DIR


class PackageGenerator:
    """
    A class used to create the basic package structure
    ...

    Attributes
    ----------

    args : dict
        Contains the info to create the package according to needs of the user

    Methods
    -------
    call()
        Creates the package structure
    """

    def __init__(self, args):
        """
        Parameters
        ----------
        args : dict
            Contains the info to create the package
            according to needs of the user.
        """
        self._package_name = args.get('name', '')
        self.path = args.get('path', '')
        self.tests = args.get('tests', True)
        self._defaults(args)

    def call(self):
        """
        Creates the package structure
        """
        try:
            self._is_name_empty()
            self._main_package_structure()
            self._tests_directory()
            self._create_default_files()
            self._create_custom_files()
        except DirectoryExistsError as dir_error:
            print(f'{fg(1)} An error has occurred:{attr(0)} {dir_error}')
        except ForgottenNameError as name_error:
            print(f'{fg(1)} An error has occurred: {attr(0)} {name_error}')

    def _create_custom_files(self):
        if self.pipfile:
            self._create_file(PIPFILE)
        if self.code_of_conduct:
            self._create_file(CODE_OF_CONDUCT)
        if self.license:
            self._create_file(LICENSE)

    def _create_dir(self, dir_name):
        structure = os.path.join(self.path, self._package_name,
                                 dir_name)
        if not os.path.exists(structure):
            os.makedirs(structure)
            self._create_init_file(structure)
        else:
            raise DirectoryExistsError('The directory already exists')

    def _create_file(self, filename):
        path_to_file = os.path.join(self.path, self._package_name)
        if os.path.isdir(path_to_file):
            os.mknod(os.path.join(path_to_file, filename))

    def _create_default_files(self):
        self._create_file(SETUP)
        self._create_file(README)
        self._create_file(REQUIREMENTS)
        self._create_file(GITIGNORE)

    def _create_init_file(self, structure):
        os.mknod(os.path.join(structure, INIT_FILE))

    def _defaults(self, args):
        self.pipfile = args.get('pipfile', True)
        self.license = args.get('license', True)
        self.code_of_conduct = args.get('code_of_conduct', True)

    def _is_name_empty(self):
        if not self.package_name:
            raise ForgottenNameError('The name is empty!')

    def _main_package_structure(self):
        self._create_dir(self.package_name)

    def _tests_directory(self):
        self._create_dir(TESTS_DIR)

    @property
    def package_name(self):
        """Replaces the - character with _ character
        """
        return self._package_name.replace('-', '_')
