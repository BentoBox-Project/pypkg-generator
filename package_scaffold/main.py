import click
import package_creator


@click.command()
@click.option('--name', '-n', default='forgotten_name',
              help='The name of the package')
@click.option('--path', '-p', default='',
              help='The path where the package will be created')
@click.option('--readme/--no-readme', default=True,
              help='Create the README file or not, created by default')
@click.option('--req/--no-req', default=True,
              help='Create requirements.txt or not, created by default')
@click.option('--pipfile/--no-pipfile', default=True,
              help='Create the pipfile or not, created by default')
@click.option('--tests/--no-tests', default=True,
              help='Create test suite directory or not, created by default')
@click.option('--license/--not-license', default=True,
              help='Create the license file or not, created by default')
@click.option('--setup/--no-setup', default=True,
              help='Create setup.py file or not, created by default')
def main(name, path, readme, req, pipfile, tests, license, setup):
    args = {'name': name, 'path': path, 'readme': readme, 'req': req,
            'pipfile': pipfile, 'tests': tests, 'license': license,
            'setup': setup}
    creator = package_creator.PackageCreator(args)
    creator.call()


if __name__ == '__main__':
    main()
