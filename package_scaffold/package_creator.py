import os

from .exceptions import DirectoryExistsError


class PackageCreator:
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
        self._package_name = args.get('name', 'forgotten_name')
        self.path = args.get('path', '')
        self.tests = args.get('tests', True)
        self._init_files(args)

    def call(self):
        """
        Creates the package structure
        """
        try:
            self._main_package_structure()
            self._tests_directory()
            self._make_config_files()
        except DirectoryExistsError as dir_error:
            print(f'An error has occurred: {dir_error}')

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

    def _create_init_file(self, structure):
        os.mknod(os.path.join(structure, '__init__.py'))

    def _init_files(self, args):
        self.readme = args.get('readme', True)
        self.requirements = args.get('req', True)
        self.pipfile = args.get('pipfile', True)
        self.license = args.get('license', True)
        self.setup = args.get('setup', True)

    def _make_config_files(self):
        self._create_file('LICENSE')
        self._create_file('setup.py')
        self._create_file('Pipfile')
        self._create_file('README.md')
        self._create_file('requirements.txt')

    def _main_package_structure(self):
        self._create_dir(self.package_name)

    def _tests_directory(self):
        self._create_dir('tests')

    @property
    def package_name(self):
        return self._package_name.replace('-', '_')
