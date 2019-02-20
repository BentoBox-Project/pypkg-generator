# -*- coding: utf-8 -*-
"""Main Function and entry point of the package

This script requires that `click` be installed within the Python
environment you are running this script in.

This file contains the following functions:

    * conduct_option - Returns the conduct file option
    * license_option - Returns the license file option
    * pipfile_option - Returns the pipfile file option
    * main - the main function of the script

"""

import click
from colored import fg, attr

from pypkg_generator import package_generator


@click.command()
@click.option('--name', '-n', default='',
              help='The name of the package')
@click.option('--path', '-p', default='',
              help='The path where the package will be created')
@click.option('--tests/--no-tests', default=True,
              help='Create test suite directory or not, created by default')
def main(name, path, tests):
    """Executes the entire program

    Parameters
    ----------
    name : str
      The name of the new package
    path : str
      The path of the new package. If it is not provided, the package
      is created in the current directory
    tests : bool
      If it is true, the tests sub-directory is created.
    """
    license_file = click.confirm(license_option())
    conduct_file = click.confirm(conduct_option())
    pipfile = click.confirm(pipfile_option())
    args = {'name': name, 'path': path, 'tests': tests,
            'license': license_file, 'code_of_conduct': conduct_file,
            'pipfile': pipfile}
    creator = package_generator.PackageGenerator(args)
    creator.call()


def conduct_option():
    """Returns the conduct file option"""
    return f'{fg(2)} Do you want to include a code of conduct file? {attr(0)}'


def license_option():
    """Returns the license file option"""
    return f'{fg(2)} Do you want to include a license file? {attr(0)}'


def pipfile_option():
    """Returns the pipfile file option"""
    return f'{fg(2)} Do you want to include a Pipfile file? {attr(0)}'


if __name__ == '__main__':
    main()
